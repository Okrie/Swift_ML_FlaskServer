# -*- coding: utf8 -*-
"""
Date : 2023-09-21 03:00
Author : Okrie
Description : service/userData.py 분리
Version : 0.4
"""

from flask import Blueprint, jsonify
from . import steam

userservice = Blueprint('userservice', __name__)


def getUserid(userid):
    return steam.users.search_user(userid)


def getUserDetail(steamid):
    return steam.users.get_user_details(steamid)

def getUserFriends(steamid):
    return steam.users.get_user_friends_list(steamid)

def getuserGames(steamid):
    return steam.users.get_owned_games(steamid)

def getuserDetails(steamid):
    userprofile = steam.users.get_user_details(steamid)
    level = steam.users.get_user_steam_level(steamid)
    badges = steam.users.get_user_badges(steamid)
    return jsonify({"steamid" : steamid, "level" : level, 'badges' : badges, 'userprofile' : userprofile})