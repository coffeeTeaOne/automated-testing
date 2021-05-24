#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_register.py
# @Time      :2021/5/23 11:40
# @author    :Harry
import pytest
import requests
import ddt

@ddt.ddt
class TestRegister():
    @ddt.file_data(r'D:\WorkSpaces\ITFAutoDemo\register.yaml')
    def test_register(self, **case_data):
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
    pytest.main(['test_register.py'])

