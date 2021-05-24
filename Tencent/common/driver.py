#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :driver.py
# @Time      :2021/5/9 15:23
# @author    :Harry
from selenium import webdriver

def chrome_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()

    return driver
