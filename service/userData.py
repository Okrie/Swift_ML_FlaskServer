from steam import steam
from flask import Blueprint

userservice = Blueprint('userservice', __name__)


def getUserid(userid):
    return steam.Users.search_user(userid)


def getUserDetail(steamid):
    return steam.Users.get_user_details(steamid)


def getUserFriends(steamid):
    return steam.Users.get_user_friends_list(steamid)