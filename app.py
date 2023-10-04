# -*- coding: utf8 -*-
"""
Date : 2023-09-16 01:49
Author : Okrie
Description : Steam Game, User Data
Version : 0.3

2023-09-20 v0.2 - Module 분리
2023-09-21 v0.3 - Controller, Service로 분리
"""
from flask import jsonify, request, Blueprint
from flask import current_app as app

main = Blueprint('main', __name__, url_prefix='/')