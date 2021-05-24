#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :setting.py
# @Time      :2021/5/23 17:45
# @author    :Harry
import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(BASE_PATH, 'data')
TEMPLATE_PATH = os.path.join(BASE_PATH, 'template.txt')
CASE_PATH = os.path.join(BASE_PATH,'test_case')
print(DATA_PATH)