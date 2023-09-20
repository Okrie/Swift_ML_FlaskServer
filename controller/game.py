# -*- coding: utf8 -*-
"""
Date : 2023-09-21 03:00
Author : Okrie
Description : controller/game.py 분리
Version : 0.4
"""

from flask import request, Blueprint, jsonify
from module.bestGameCrawling import bestGame
import os, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from service.gameData import searchGames, searchGamesId

game = Blueprint('game', __name__, url_prefix='/game')


# Searching Games : Str
@game.route('/searchgames', methods = ['GET'])
def searchGames():
    search = request.args.get('search')
    try:
        result = searchGames(search)
    except:
        return jsonify({"result" : {"response_code" : 500, "reqdata" : search}})
    return jsonify({"result" : [{"retdata" : result}]})

# Searching Games : App Id
@game.route('/searchgamesid', methods = ['GET'])
def searchGamesId():
    search = request.args.get('searchid')
    try:
        result = searchGamesId(app_id=int(search))
    except:
        return jsonify({"result" : {"response_code" : 500, "reqdata" : search}})
    return jsonify({"result" : [{"retdata" : result}]})


# Steam main에서 최고 인기게임 10개의 appid 가져오기
@game.route('/bestgames')
def bestgame():
    return bestGame()