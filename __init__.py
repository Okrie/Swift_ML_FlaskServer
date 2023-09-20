# -*- coding: utf8 -*-
"""
Date : 2023-09-21 02:00
Author : Okrie
Description : __init__.py Setting
Version : 0.2
"""

# init py 분리

from flask import Flask
from decouple import config
from steam import Steam
import os, sys
import joblib
import requests
sys.path.append(os.path.abspath(os.path.dirname(__file__)))


app = Flask(__name__)

from app import main as main
from controller.user import user as user
from controller.game import game as game

app.register_blueprint(main)
app.register_blueprint(user)
app.register_blueprint(game)


if __name__ == '__main__':
    KEY = config("STEAM_API_KEY")
    steam = Steam(KEY)
    app.run(host=config("HOSTNAME"), port=config("PORT"), debug=True)