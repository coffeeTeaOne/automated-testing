#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_login.py
# @Time      :2021/5/23 11:52
# @author    :Harry
import pytest
import requests

class TestLogin():

    def test_login(self):
        url = 'http://hn216.api.yesapi.cn/?s=App.User.Login'
        data = {'app_key': '5227C53B83002D99A28D874326F07BB6',
                'username': 'tj2021',
                'password': 'ae43013c7d3446f7e9bebddd79cb3b89'}
        response = requests.post(url=url, json=data)
        result = response.json()
        print(result)
        assert 0 == result.get('data').get('err_code')

if __name__ == '__main__':
    pytest.main(['test_login.py'])
