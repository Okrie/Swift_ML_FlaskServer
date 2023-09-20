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

# @app.route('/iris', methods = ['GET'])
# def iris():
#     sepalLength = float(request.args.get('SepalLength'))
#     sepalWidth = float(request.args.get('SepalWidth'))
#     petalLength = float(request.args.get('PetalLength'))
#     petalWidth = float(request.args.get('PetalWidth'))
    
#     clf = joblib.load('Flask/data/rf_iris.h5')
#     pred = clf.predict([[sepalLength, sepalWidth, petalLength, petalWidth]])
#     return jsonify([{'result' : pred[0][:5]}])

# get rsa Key
@main.route('/rstest')
def getRsaKey():
    username = request.args.get('username')
    url = f'https://steamcommunity.com/login/getrsakey/?username={username}'
    response = requests.get(url=url)
    print(response.text)
    return response.text
