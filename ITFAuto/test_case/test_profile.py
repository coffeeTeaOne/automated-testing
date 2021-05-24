#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_register.py
# @Time      :2021/5/23 11:40
# @author    :Harry
import pytest
import requests
import ddt
import os
from config.setting import DATA_PATH

@ddt.ddt
class TestProfile():
    @ddt.file_data(os.path.join(DATA_PATH, 'profile.yaml'))
    def test_profile(self, **case_data):
            # 获取测试数据
            url = case_data.get('url')
            data = case_data.get('data')
            expect = case_data.get('expected')
            method = case_data.get('method')
            # 接口请求
            response = None
            if method == 'post':
                response = requests.post(url=url, json=data)
            elif method == 'get':
                response = requests.get(url=url, params=data)
            result = response.text
            #结果处理
            result = result.replace('":"', '=').replace('":', '=')  # 字符替换
            print(result)
            for ex in expect:
                assert ex in result

if __name__ == '__main__':
    pytest.main(['test_profile.py'])

