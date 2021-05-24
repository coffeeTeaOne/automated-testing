#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :page_base.py
# @Time      :2021/5/9 14:11
# @author    :Harry
import os
from selenium.webdriver import ActionChains
from common.base_path import PIC_PATH, LOG_PATH
from common.utils_log import MyLog

class BasePage():
    def __init__(self,driver):
        self.driver = driver
        self.base_url = 'https://ke.qq.com/'
        self.logger = MyLog('page', os.path.join(LOG_PATH,'home-2021-05-16.log'))

    def open(self,url):
        self.driver.get(url)
        self.driver.implicitly_wait(30)

    def switch_window(self):
        '''窗口切换'''
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[-1])

    def move_to_menu(self, elem):
        '''鼠标悬浮'''
        action = ActionChains(self.driver)
        action.move_to_element(elem).perform()

    def switch_frame_enter(self, frame):
        '''进入frame'''
        self.driver.switch_to.frame(frame)
        # print("进入frame")
        self.logger.info('----进入frame -----')

    def switch_frame_quit(self):
        '''退出frame'''
        self.driver.switch_to.parent_frame()
        # print("退出frame")
        self.logger.info('----- 退出frame----')

    def save_screen_pic(self, filename):
        filepath = os.path.join(PIC_PATH, filename+'.png')
        print(filepath)
        self.driver.save_screenshot(filepath)
