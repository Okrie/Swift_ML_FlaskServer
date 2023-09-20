# from Crypto.Cipher import AES
# from Crypto.Cipher.PKCS1_v1_5 import PKCS115_Cipher
# from Crypto.PublicKey import RSA
# from Crypto.Random import get_random_bytes
import hashlib
import json
import requests
from decouple import config
from flask import Flask, jsonify, request


# get rsa Key
def getRsaKey(username):
    url = f'https://steamcommunity.com/login/getrsakey/?username={username}'
    response = requests.get(url=url)
    print(response.text)
    return response

# params = {
#         "param1": "test1",
#         "param2": 123,
#         "param3": "한글"
#     }
#     res = requests.post("http://127.0.0.1:5000/handle_post", data=json.dumps(params))
#     return res.text
# steamid = '<MY_STEAMID64>'
# steampass = '<MY_STEAM_PASSWORD>'
# loginkey = hashlib.md5(bytes(steampass, 'utf-8')).hexdigest()
# blob32 = get_random_bytes(32)

# getrsa_url = 'https://steamcommunity.com/login/getrsakey/'
# getrsa_data = {'username': '<MY_STEAM_USERNAME>'}

# getrsa_resp = requests.get(getrsa_url, params=getrsa_data)
# response = json.loads(getrsa_resp.text)
# if response.get('success'):
#     steam_publickey_mod = response.get('publickey_mod')
#     steam_publickey_mod = int(steam_publickey_mod, 16)
#     steam_publickey_exp = response.get('publickey_exp')
#     steam_publickey_exp = int(steam_publickey_exp, 16)
#     steam_rsa_key = RSA.construct((steam_publickey_mod, steam_publickey_exp))
#     steam_rsa = PKCS115_Cipher(steam_rsa_key)

# if steam_rsa_key.can_encrypt():
#     sessionkey = steam_rsa.encrypt(blob32)
#     if type(sessionkey) is tuple:
#         sessionkey = sessionkey[0]
#     steam_aes = AES.new(blob32)
#     encrypted_loginkey = steam_aes.encrypt(loginkey)

# if all([steamid, sessionkey, encrypted_loginkey]):
#     authenticate_user_url = (
#         'https://api.steampowered.com/ISteamUserAuth/AuthenticateUser/v0001')
#     authenticate_user_json = {
#         'steamid': steamid,
#         'sessionkey': sessionkey,
#         'encrypted_loginkey': encrypted_loginkey,
#     }