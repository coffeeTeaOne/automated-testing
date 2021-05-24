#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :demo.py
# @Time      :2021/5/23 10:57
# @author    :Harry

import requests

url = 'http://hn216.api.yesapi.cn/?s=App.User.Register'
data = {'app_key':'5227C53B83002D99A28D874326F07BB6',
        'username':'tj2021',
        'password':'ae43013c7d3446f7e9bebddd79cb3b89'}

# get 请求
# res = requests.get(url=url, params=data)

# post请求
header = {
    'Referer':'http://hn216.api.yesapi.cn',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
}


res = requests.post(url=url, json=data, headers=header)
res_lits = res.text

print('文本报文：', res_lits)
print('json 报文', res.json().get('data').get('err_code')) # 具体字段值

print(res.headers)       # 响应头信息，session
print(res.status_code)  # 请求响应应答码：200,300,400,500 系列应答码

