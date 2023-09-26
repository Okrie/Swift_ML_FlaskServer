# -*- coding: utf8 -*-
"""
Date : 2023-09-21 03:00
Author : Okrie
Description : service/gameData.py 분리
Version : 0.4
"""

from flask import Blueprint
from . import steam
from bs4 import BeautifulSoup
import urllib.request as req
import json

gameservice = Blueprint('gameservice', __name__)

# Searching Games : Str
def searchGamesService(search):
    return steam.apps.search_games(search, country="KR")

# Searching Games : App Id
def searchGamesIdService(search):
    return steam.apps.get_app_details(app_id=search)


# Searching Games : App Id
def searchGamesIdReService(search):
    url = f"https://store.steampowered.com/app/{search}"

    res = req.urlopen(url)
    soup = BeautifulSoup(res, "html.parser")

    appid = search
    img_link = soup.select_one('#gameHeaderImageCtn > img').attrs['src']
    name = soup.select_one('#appHubAppName').text
    price = soup.select_one('div.game_purchase_action div.game_purchase_price.price').text.strip()

    response = req.urlopen(f'https://store.steampowered.com/api/appdetails?appids={search}')
    res = json.load(response)
    detail_info = res[f'{search}']['data']['about_the_game']
    return appid, img_link, name, price, detail_info