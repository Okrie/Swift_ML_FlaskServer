# -*- coding: utf8 -*-
"""
Date : 2023-09-21 02:00
Author : Okrie
Description : service/__init__.py Setting
Version : 0.2
"""

from decouple import config
from steam import Steam

KEY = config("STEAM_API_KEY")
steam = Steam(KEY)
