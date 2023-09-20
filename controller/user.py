from flask import request, Blueprint, jsonify
from service.userData import getUserid, getUserDetail, getUserFriends

user = Blueprint('user', __name__, url_prefix='/user')


# User 검색
# 2023-09-20 v0.2 module userData 분리
# 2023-09-21 v0.3 controller로 분리
@user.route('/', methods = ['GET'])
def index():
    try:
        result = getUserid(request.args.get('userid'))
    except:
        return jsonify({"result" : {"response_code" : 401, "reqdata" : request.args.get('userid')}})
    return result

# User의 상세정보
# 2023-09-20 v0.2 module userData 분리
# 2023-09-21 v0.3 controller로 분리
@user.route('/getuser', methods = ['GET'])
def getuser():
    try:
        result = getUserDetail(request.args.get('steamid'))
    except:
        return jsonify({"result" : {"response_code" : 401, "reqdata" : request.args.get('steamid')}})
    return result

# User의 친구목록
# 2023-09-20 v0.2 module userData 분리
# 2023-09-21 v0.3 controller로 분리
@user.route('/getuserfriends', methods = ['GET'])
def getuserFriends():
    try:
        result = getUserFriends(steam_id=request.args.get('steamid'))
    except:
        return jsonify({"result" : {"response_code" : 401, "reqdata" : request.args.get('steamid')}})
    return result


# User가 보유중인 game
# 2023-09-20 v0.2 module userData 분리
# 2023-09-21 v0.3 controller로 분리
@user.route('/getusergames', methods = ['GET'])
def getuserGames():
    try:
        result = steam.users.get_owned_games(steam_id=request.args.get('steamid'))
    except:
        return jsonify({"result" : {"response_code" : 500, "reqdata" : request.args.get('steamid')}})
    return result


# User 상세정보
# 2023-09-20 v0.2 module userData 분리
# 2023-09-21 v0.3 controller로 분리
@user.route('/getuserdetails', methods = ['GET'])
def getuserDetails():
    steamid = request.args.get('steamid')
    try:
        userprofile = steam.users.get_user_details(steam_id=steamid)
        level = steam.users.get_user_steam_level(steam_id=steamid)
        badges = steam.users.get_user_badges(steam_id=steamid)
    except:
        return jsonify({"result" : {"response_code" : 500, "reqdata" : steamid}})
    return jsonify({"result" : {"retdata" : [{"steamid" : steamid, "level" : level, 'badges' : badges, 'userprofile' : userprofile}]}})