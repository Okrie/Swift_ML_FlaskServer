from flask import request, Blueprint, jsonify
from module.bestGameCrawling import bestGame

game = Blueprint('game', __name__, url_prefix='/game')


# Searching Games : Str
@game.route('/searchgames', methods = ['GET'])
def searchGames():
    search = request.args.get('search')
    try:
        result = steam.apps.search_games(search, country="KR")
    except:
        return jsonify({"result" : {"response_code" : 500, "reqdata" : search}})
    return jsonify({"result" : [{"retdata" : result}]})

# Searching Games : App Id
@game.route('/searchgamesid', methods = ['GET'])
def searchGamesId():
    search = request.args.get('searchid')

    try:
        result = steam.apps.get_app_details(app_id=int(search), country="KR")
    except:
        return jsonify({"result" : {"response_code" : 500, "reqdata" : search}})
    return jsonify({"result" : [{"retdata" : result}]})


# Steam main에서 최고 인기게임 10개의 appid 가져오기
@game.route('/bestgames')
def bestgame():
    return bestGame()