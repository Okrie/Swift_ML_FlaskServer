# -*- coding: utf8 -*-
"""
Date : 2023-09-17 02:13
Author : Okrie
Description : Steam Scrapy Game Data
Version : 0.1
"""

import json
import urllib.request as req

class SteamCustomAPI:
    """
    Steam App Custom API
    Using https://steamapis.com/
    """

    def __init__(self):
        """Constructor for default Settings"""
        self.__allGameurl = "http://api.steampowered.com/ISteamApps/GetAppList/v0002/?l=koreana&format=json"
        self.__detailGameurl = "https://store.steampowered.com/api/appdetails?l=koreana&appids="
        self.__country = "&country=KR"

    def getAllGames(self):
        """
        Get All Steam Games

        Detail:
            applist -> apps -> {appid, name}
        :param:
            No Parameter
        """
        response = req.urlopen(self.__allGameurl)
        data = json.load(response)
        return data
