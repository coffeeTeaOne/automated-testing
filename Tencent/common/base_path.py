#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :base_path.py
# @Time      :2021/5/16 11:56
# @author    :Harry
import os

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_PATH)
LOG_PATH = os.path.join(BASE_PATH, 'log')

PIC_PATH = os.path.join(LOG_PATH,'pic')
print(PIC_PATH)

REPORT_PATH = os.path.join(BASE_PATH, 'report')