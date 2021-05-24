#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :page_login.py
# @Time      :2021/5/10 9:34
# @author    :Harry
import time
from selenium.webdriver.common.by import By
from page.page_base import BasePage

class LoginPage(BasePage):

    #定位器
    locator_login_btn = (By.XPATH, '//*[@id="js-mod-entry-index"]/a')  #登录按钮
    locator_login_user = (By.XPATH, '//*[@id="qlogin_list"]/a')
    def login_elem_login_btn(self):
        self.driver.find_element(*self.locator_login_btn).click()
        time.sleep(3)

    def login(self):
        self.open('https://ke.qq.com/')
        #登录
        iframe = self.driver.find_element(By.XPATH,'/html/body/div[2]/section/div[2]/div/div/iframe')
        self.driver.switch_to.frame(iframe)
        # self.switch_frame_enter(iframe)

        self.driver.find_element(*self.locator_login_user).click()
        print("登录成功")
        time.sleep(3)
        self.driver.switch_to.parent_frame()
        # self.switch_frame_quit()
