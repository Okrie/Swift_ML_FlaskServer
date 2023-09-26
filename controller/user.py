# -*- coding: utf8 -*-
"""
Date : 2023-09-21 03:00
Author : Okrie
Description : controller/user.py 분리
Version : 0.4
"""

from flask import request, Blueprint, jsonify
import os, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from service.userData import getUseridService, getUserDetailService, getUserFriendsService, getuserGamesService, getuserDetailsService
from .recommend import recommended, save_to_csv
import pandas as pd

user = Blueprint('user', __name__, url_prefix='/user')


# User 검색
# 2023-09-20 v0.2 module userData 분리
# 2023-09-21 v0.3 controller로 분리
@user.route('/', methods = ['GET'])
def index():
    try:
        result = getUseridService(request.args.get('userid'))
    except:
        return jsonify({"result" : {"response_code" : 500, "reqdata" : request.args.get('userid')}})
    return result

# User의 상세정보
# 2023-09-20 v0.2 module userData 분리
# 2023-09-21 v0.3 controller로 분리
@user.route('/getuser', methods = ['GET'])
def getuser(LOGIN=False):
    steamid = request.args.get('steamid')
    try:
        request.args.get('login')
        LOGIN = True
    except:
        LOGIN = False

    # try:
    result = getUserDetailService(steamid)
    if LOGIN:
        resp = getuserGamesService(steamid)
        res = save_to_csv(steamid, resp)
        if res:
            return recommended(steamid)
        else:
            return jsonify({"result" : {"response_code" : 402, "reqdata" : steamid}})
    # except:
    #     return jsonify({"result" : {"response_code" : 401, "reqdata" : steamid}})
    return result

# User의 친구목록
# 2023-09-20 v0.2 module userData 분리
# 2023-09-21 v0.3 controller로 분리
@user.route('/getuserfriends', methods = ['GET'])
def getuserFriends():
    try:
        result = getUserFriendsService(request.args.get('steamid'))
    except:
        return jsonify({"result" : {"response_code" : 401, "reqdata" : request.args.get('steamid')}})
    return result


# User가 보유중인 game
# 2023-09-20 v0.2 module userData 분리
# 2023-09-21 v0.3 controller로 분리
@user.route('/getusergames', methods = ['GET'])
def getuserGames():
    try:
        result = getuserGamesService(request.args.get('steamid'))
    except:
        return jsonify({"result" : {"response_code" : 500, "reqdata" : request.args.get('steamid')}})
    return result


# User 상세정보
# 2023-09-20 v0.2 module userData 분리
# 2023-09-21 v0.3 controller로 분리
@user.route('/getuserdetails', methods = ['GET'])
def getuserDetails():
    steamid = request.args.get('steamid')
    try:
        result = getuserDetailsService(steamid)
    except:
        return jsonify({"result" : {"response_code" : 500, "reqdata" : steamid}})
    return jsonify({"result" : {"retdata" : [result]}})