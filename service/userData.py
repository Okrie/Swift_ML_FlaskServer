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


def getUseridService(userid):
    return steam.users.search_user(userid)

def getUserDetailService(steamid):
    return steam.users.get_user_details(steamid)

def getUserFriendsService(steamid):
    return steam.users.get_user_friends_list(steamid)

def getuserGamesService(steamid):
    return steam.users.get_owned_games(steamid)

def getuserDetailsService(steamid):
    userprofile = steam.users.get_user_details(steamid)
    level = steam.users.get_user_steam_level(steamid)
    badges = steam.users.get_user_badges(steamid)
    return {"steamid" : steamid, "level" : level, 'badges' : badges, 'userprofile' : userprofile}