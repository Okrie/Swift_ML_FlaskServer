# -*- coding: utf8 -*-
"""
Date : 2023-09-21 02:00
Author : Okrie
Description : service/__init__.py Setting
Version : 0.2
"""

from dotenv import load_dotenv
from steam import Steam
import os


KEY = os.environ.get("STEAM_API_KEY")
steam = Steam(KEY)
