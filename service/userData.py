# -*- coding: utf8 -*-
"""
Date : 2023-09-21 03:00
Author : Okrie
Description : service/userData.py 분리
Version : 0.4
"""

from flask import Blueprint
from . import steam

userservice = Blueprint('userservice', __name__)

# 유저 NickName으로 정보 검색
def getUseridService(userid):
    """
        User NickName
        getUseridService(NICKNAME:String)
        :args:
            userid
    """
    return steam.users.search_user(userid)


# 유저 Steamid로 상세정보 검색
def getUserDetailService(steamid):
    return steam.users.get_user_details(steamid)

# 유저 steamid로 해당 유저의 친구 목록 호출
def getUserFriendsService(steamid):
    return steam.users.get_user_friends_list(steamid)

# 유저 steamid로 보유 중인 게임 목록 호출
def getuserGamesService(steamid):
    return steam.users.get_owned_games(steamid)

# 유저 steamid로 개인 페이지에 노출할 정보 호출
def getuserDetailsService(steamid):
    userprofile = steam.users.get_user_details(steamid)
    level = steam.users.get_user_steam_level(steamid)
    badges = steam.users.get_user_badges(steamid)
    return {"steamid" : steamid, "level" : level, 'badges' : badges, 'userprofile' : userprofile}