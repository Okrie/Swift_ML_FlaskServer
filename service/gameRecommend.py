# -*- coding: utf8 -*-
"""
Date : 2023-09-27 02:00
Author : Okrie
Description :   사용자의 게임 보유 목록으로 게임 장르 추천
Version : 0.1
"""

from flask import Blueprint, jsonify
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder
from . import steam
import json
import pandas as pd
import numpy as np
import datetime
import re
import urllib.request as req


recommendedservice = Blueprint('recommendedservice', __name__)


# 유저의 보유 게임 및 상세정보 가공으로 연관성 분석
# 장르 기반으로 추천
def getUserownRecommendService(steamid, MAX_SIZE=50):
    user_df = pd.read_csv(f'/home/okrie/Desktop/FLASK/Swift_ML_FlaskServer/Data/{steamid}.csv')
    
    return_dict = []
    k = 0

    # 최대값이 100 user 보유게임 체크하여 개수 정의
    if len(user_df) > MAX_SIZE:
        MAX_SIZE = 50
    else:
        MAX_SIZE = len(user_df)

    # 보유중인 게임 데이터 받아오기
    while k < MAX_SIZE:
        for j in range(MAX_SIZE):
            i = user_df.loc[j, 'appid']
            detail_url = 'https://store.steampowered.com/api/appdetails?country=KR&appids=' + str(i)

            response = req.urlopen(detail_url)
            result = json.load(response)
            if result[str(i)]['success'] != False:
                rdata = result[str(i)]['data']
                return_dict.append(rdata)
            k += 1

    # 받은 데이터 확인
    rec_df = pd.DataFrame(return_dict)
    
    # 필요 없는 컬럼 삭제
    del_columns = ['type', 'name', 'is_free', 'detailed_description', 'about_the_game', 'short_description', 'header_image', 'capsule_image', 'capsule_imagev5', \
        'website', 'pc_requirements', 'mac_requirements', 'linux_requirements', 'package_groups', 'screenshots', 'movies', 'release_date', 'support_info', 'background', \
        'background_raw', 'content_descriptors', 'controller_support', 'packages', 'dlc', 'legal_notice', 'demos', 'reviews', 'ext_user_account_notice'
    ]
    rec_df.drop(columns=del_columns, inplace=True)

    # 나이 object -> int
    rec_df['required_age'] = rec_df['required_age'].astype('int')

    # 컬럼 재정의
    columns = ['appid', 'required_age', 'supported_languages', 'developers', 'publishers', 'platforms', 'categories', 'genres', 'achievements', 'metacritic', 'recommendations', 'price_overview']
    rec_df.columns = columns

    # 유저 데이터와 합치기
    user_concat = pd.merge(user_df, rec_df)

    # languages
    # Eng, Kor 포함 유무 확인
    pattern = r'(Eng|Kor)'
    for i in range(0, len(user_concat)):
        if len(re.findall(pattern, str(user_concat['supported_languages'].values[i]))) == 0:
            user_concat['supported_languages'].values[i] = False
        else:
            user_concat['supported_languages'].values[i] = True


    # 거의 다 다른 정보들이어서 컬럼 삭제
    del_columns = ['developers', 'publishers']
    user_concat.drop(columns=del_columns, inplace=True)

    # metacritic, recommendations, price_overview 가공
    # NaN 정보는 0으로 대체
    user_concat['metacritic'].fillna(0, inplace=True)
    user_concat['recommendations'].fillna(0, inplace=True)
    user_concat['price_overview'].fillna(0, inplace=True)

    # user_concat['metacritic']
    user_concat['metacritic'] = user_concat['metacritic'].apply(lambda x: x.get('score') if isinstance(x, dict) else 0)

    # user_concat['recommendations']
    user_concat['recommendations'] = user_concat['recommendations'].apply(lambda x: x.get('total') if isinstance(x, dict) else 0)

    # user_concat['price_overview']
    user_concat['price_overview'] = user_concat['price_overview'].apply(lambda x: x.get('final')/100 if isinstance(x, dict) else 0)

    user_concat['platforms'].fillna(0, inplace=True)

    user_concat['windows'] = user_concat['platforms'].apply(lambda x: x.get('windows', False)).astype(int)
    user_concat['mac'] = user_concat['platforms'].apply(lambda x: x.get('mac', False)).astype(int)
    user_concat['linux'] = user_concat['platforms'].apply(lambda x: x.get('linux', False)).astype(int)
    user_concat.drop(columns='platforms', inplace=True)

    # categories one-hot encoding
    user_concat['categories'][0][0]['description']

    temp_list = []
    for i in range(len(user_concat['categories'])):
        temp_list.append(user_concat['categories'][i][0]['description'])

    user_concat['categories'] = temp_list

    # single = 1, multi = 0
    user_concat['single_player'] = user_concat['categories'].apply(lambda x: 1 if x == 'Single-player' else 0)
    user_concat.drop(columns='categories', inplace=True)

    # achievement 개수
    user_concat['achievements'] = user_concat['achievements'].apply(lambda x: x.get('total') if isinstance(x, dict) else 0)

    # 장르 분리
    temp_list = []
    for i in range(len(user_concat)):
        temp_list = ', '.join(item['description'] for item in user_concat['genres'][i])
        user_concat['genres'][i] = temp_list



    ### 연관성 분석

    # List 형식으로 변환
    genre_list = user_concat['genres'].apply(lambda x: x.split(', '))

    # 장르의 연관성 분석을 위한 행렬 컬럼 만들기
    genre_unique = []
    for i in genre_list:
        for j in i:
            genre_unique.append(j)
            
    gn_un = pd.DataFrame(genre_unique)
    gn_col = list(gn_un[0].unique())

    # Association Anaylsis Matrix
    # 동일한 크기의 배열 전부 0으로 초기화
    gn_aa = pd.DataFrame(np.zeros(shape=(len(genre_list), len(gn_col))), columns=gn_col, dtype='int')
    k = 0
    for i in genre_list:
        for j in i:
            gn_aa.loc[k, j] = 1
        k += 1

    # 연관도 계산
    te = TransactionEncoder()
    te_ary = te.fit(genre_list).transform(genre_list, sparse=True)
    te_df = pd.DataFrame.sparse.from_spmatrix(te_ary, columns=te.columns_)

    frequent_itemset = apriori(
        gn_aa,
        min_support=0.005, 
        max_len=3, 
        use_colnames=True, 
        verbose=1 
    )

    frequent_itemset['length'] = frequent_itemset['itemsets'].map(lambda x: len(x))
    frequent_itemset.sort_values('support',ascending=False,inplace=True)

    association_rules_df = association_rules(
        frequent_itemset, 
        metric='confidence', 
        min_threshold=0.005,
    )

    # 5개의 결과 출력
    # Support : 지지도
    # Confidence : 신뢰도
    # Lift : 향상도

    # max_i = 1
    # for i, row in association_rules_df.iterrows():
    #     print("Rule: " + list(row['antecedents'])[0] + " => " + list(row['consequents'])[0])

    #     print("Support: " + str(round(row['support'],2)))

    #     print("Confidence: " + str(round(row['confidence'],2)))
    #     print("Lift: " + str(round(row['lift'],2)))
    #     print("=====================================")
    #     if i==max_i:
    #         break

    temp = []
    temp.append(association_rules_df["antecedents"].apply(lambda x: ', '.join(list(x))).astype("unicode"))
    temp.append(association_rules_df["consequents"].apply(lambda x: ', '.join(list(x))).astype("unicode"))

    return jsonify({'result' : {'rule' : temp[0][0], 'to' : temp[0][1], 'support' : str(round(association_rules_df['support'][0],2)), 'confidence' : str(round(association_rules_df['confidence'][0],2)), 'lift' : str(round(association_rules_df['lift'][0],2))}})

# 유저 데이터 정제
def save_to_csvService(steamid, result):
    try:
        games = result['games']
        game_df = pd.DataFrame(games)

        # 필요 없는 컬럼 삭제
        del game_df['has_community_visible_stats']
        del game_df['img_icon_url']
        del game_df['playtime_linux_forever']
        del game_df['playtime_mac_forever']
        del game_df['playtime_windows_forever']
        del game_df['content_descriptorids']
        del game_df['has_leaderboards']
        del game_df['playtime_disconnected']

        # ctime to datetime
        # 마지막 플레이타임 unix to datetime
        temp = game_df[:]
        for i in range(len(temp)):
            if temp.rtime_last_played[i] != 0:
                temp.rtime_last_played[i] = datetime.datetime.utcfromtimestamp(temp.rtime_last_played[i]).strftime('%Y-%m-%d %H:%M:%S')

        # 한번도 플레이 하지 않은 항목 제거
        temp = temp[temp.playtime_forever != 0]

        # playtime 2weeks 컬럼 분해
        # play_2weeks = playtime_2weeks == NaN => False
        # play_2weeks = playtime_2weeks != NaN => True
        temp['play_2weeks'] = temp.playtime_2weeks.notnull()

        # playtime_2weeks NaN일 경우 0으로 대체
        temp.loc[temp.playtime_2weeks.isnull(), 'playtime_2weeks'] = 0

        # 받아 오기 전 유저가 플레이 많이 한 게임 100개 로드
        MAX_SIZE = 50
        if len(temp) > MAX_SIZE:
            MAX_SIZE = 50
        else:
            MAX_SIZE = len(temp)
        user_df = temp.sort_values(by='playtime_forever', ascending=False)[:MAX_SIZE]

        # index 초기화
        user_df.reset_index(drop=True, inplace=True)

        user_df.to_csv(f'/home/okrie/Desktop/FLASK/Swift_ML_FlaskServer/Data/{steamid}.csv', index=False)
    except:
        return False
    return True