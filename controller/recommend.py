# -*- coding: utf8 -*-
"""
Date : 2023-09-27 02:00
Author : Okrie
Description :   사용자의 게임 보유 목록으로 게임 장르 추천
Version : 0.1
"""

from flask import request, Blueprint, jsonify
import os, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from service.gameRecommend import recommendedservice, save_to_csvService, getUserownRecommendService

recommend = Blueprint('recommend', __name__, url_prefix='/recommend')

# recommended games
# https://api.steampowered.com/ISteamApps/GetAppList/v0002/?tag=RPG&tag=Indie&l=kr


# 유저 데이터 정제
@recommend.route('/scv')
def save_to_csv(steamid, result):
    return save_to_csvService(steamid, result)
    


@recommend.route('/')
def recommended(steamid):
    return getUserownRecommendService(steamid)