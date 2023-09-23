from bs4 import BeautifulSoup
import urllib.request as req
import re

url = "https://store.steampowered.com/"

res = req.urlopen(url)
soup = BeautifulSoup(res, "html.parser")


def bestGameService():
    dict_list = {'appid' : [], 'detail_link' : [], 'name' : [], 'price' : []}

    resp = soup.select('div.tab_content > a.tab_item')

    i = 0
    for res in resp:
        # print(res.attrs['data-ds-appid'])
        # best_dict_list
        dict_list['appid'].append(res.attrs['data-ds-appid'])
        dict_list['detail_link'].append(res.attrs['href'])
        dict_list['name'].append(res.select_one('div.tab_item_name').text)
        dict_list['price'].append(res.select_one('div.discount_final_price').text)
        i += 1
        if i == 9:
            break

    return dict_list
