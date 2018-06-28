#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/6/28 10:45
# @Author  : Weiqiang.long
# @Site    : 
# @File    : case3.py
# @Software: PyCharm

import json
a = '{"status":0,"message":"ok","results":[{"name":"park","location":{"lat":39.498402,"lng":116.007069},"address":"xx road","street_id":"32541349605e7ae96ca3cc1e","detail":1,"uid":"32541349605e7ae96ca3cc1e"}]}'
jsonData = json.loads(a)
print(jsonData)
print(type(jsonData))
print(jsonData['results'][0]['location']['lat'])
print(jsonData['results'][0]['location']['lng'])
print(jsonData['results'][0]['address'])