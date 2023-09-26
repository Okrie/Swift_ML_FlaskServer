# -*- coding: utf8 -*-
"""
Date : 2023-09-24 23:10
Author : Okrie
Description :   best game / 스팀 추천리스트 호출
                Steam site 내 추천 리스트 항목 n개 호출
Version : 0.1
"""

from bs4 import BeautifulSoup
import urllib.request as req

url = "https://store.steampowered.com/"

res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")


def bestGameService(DEFAULT_COUNT = 9):
    dict_list = {'appid' : [], 'detail_link' : [], 'name' : [], 'price' : []}

    resp = soup.select('div.tab_content > a.tab_item')

    i = 0
    for res in resp:
        # print(res.attrs['data-ds-appid'])
        # best_dict_list
        dict_list['appid'].append(res.attrs['data-ds-appid'])
        dict_list['detail_link'].append(res.attrs['href'])
        dict_list['name'].append(res.select_one('div.tab_item_name').text)
        dict_list['price'].append(res.select_one('div.discount_final_price').text)
        i += 1
        if i == DEFAULT_COUNT:
            break

    return dict_list
