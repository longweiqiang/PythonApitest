# -*- coding: UTF-8 -*-
# @Time       : 2018/6/29 22:49
# @Author     : Weiqiang.long
# @File       : jsonconfig.py
# @Software   : PyCharm
# @Description: 
# @TODO       :

# -*- coding: utf-8 -*-

import json
import os
BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
JSON_PATH = os.path.join(BASE_PATH, 'data', 'json', 'data.json')
print(JSON_PATH)

import time











def store(data):
    with open(JSON_PATH, 'a') as json_file:
        j = json.dumps((data),sort_keys=True, indent=4)
        json_file.write(j)
        print(j)

# def load():
#     with open(JSON_PATH, 'a') as json_file:
#         data = json.load(json_file)
#         return data





if __name__ == "__main__":

    data = {}
    data["last"]=time.strftime("%Y%m%d")
    store(data)

    # data = load()
    # print(data["last"])