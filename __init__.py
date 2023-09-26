# -*- coding: utf8 -*-
"""
Date : 2023-09-21 02:00
Author : Okrie
Description : __init__.py Setting
Version : 0.3
"""

# init py 분리

from flask import Flask
from steam import Steam
import os, sys
import joblib
import requests
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

app = Flask(__name__)


KEY = os.environ.get("STEAM_API_KEY")
steam = Steam(KEY)

from app import main as main
from controller.user import user as user
from controller.game import game as game
# v0.3 recommend 추가
from controller.recommend import recommend as recommend

app.register_blueprint(main)
app.register_blueprint(user)
app.register_blueprint(game)
# v0.3 recommend 추가
app.register_blueprint(recommend)

if __name__ == '__main__':
    app.run(host=os.environ.get("FLASK_RUN_HOST"), port=os.environ.get("FLASK_RUN_PORT"), debug=os.environ.get("FLASK_DEBUG"))
    