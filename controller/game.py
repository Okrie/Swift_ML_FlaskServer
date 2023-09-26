# -*- coding: utf8 -*-
"""
Date : 2023-09-21 03:00
Author : Okrie
Description :   controller/game.py 분리
                Search game / 게임 이름, appid로 검색
                best game / 스팀 추천리스트 호출
Version : 0.5
"""

from flask import request, Blueprint, jsonify
import os, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from module.bestGameCrawling import bestGameService
from service.gameData import searchGamesService, searchGamesIdService, searchGamesIdReService

game = Blueprint('game', __name__, url_prefix='/game')


# Searching Games : Str
@game.route('/searchgames', methods = ['GET'])
def searchGames():
    search = request.args.get('search')
    try:
        result = searchGamesService(search)
    except:
        return jsonify({"result" : {"response_code" : 500, "reqdata" : search}})
    return jsonify({"result" : [{"retdata" : result}]})

# Searching Games : App Id
# 2023-09-27 v0.05 detail_info 정보 추가
@game.route('/searchgamesid', methods = ['GET'])
def searchGamesId():
    search = request.args.get('searchid')
    try:
        result = searchGamesIdService(app_id=int(search))
    except:
        appid, img_link, name, price, detail_info = searchGamesIdReService(int(search))
        return jsonify({'result' : {'appid' : appid, 'img_link' : img_link, 'name' : name, 'detail_info' : detail_info, 'price' : price}})
        # return jsonify({"result" : {"response_code" : 500, "reqdata" : search}})
    return jsonify({"result" : [{"retdata" : result}]})


# Steam main에서 최고 인기게임 10개의 appid 가져오기
@game.route('/bestgames')
def bestgame():
    return bestGameService()

