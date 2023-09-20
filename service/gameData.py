# -*- coding: utf8 -*-
"""
Date : 2023-09-21 03:00
Author : Okrie
Description : service/gameData.py 분리
Version : 0.4
"""

from flask import Blueprint
from . import steam

gameservice = Blueprint('gameservice', __name__)

# Searching Games : Str
def searchGames(search):
    return steam.apps.search_games(search, country="KR")

# Searching Games : App Id
def searchGamesId(search):
    return steam.apps.get_app_details(app_id=int(search), country="KR")
