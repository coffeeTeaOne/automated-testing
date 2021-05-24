#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :page_detail.py
# @Time      :2021/5/9 11:36
# @author    :Harry
from selenium.webdriver.common.by import By
from page.page_base import BasePage

class DetailPage(BasePage):
    #元素定位器
    locator_ele_buy = (By.XPATH, '//*[@id="js_btn_bar"]/span[1]/span/button/span[2]')
    locator_ele_play = (By.XPATH,'//*[@id="txvideo-player-container"]/div[2]/div')

    def detail_ele_buy(self):
        assert_title = self.driver.title
        self.driver.find_element(*self.locator_ele_buy).click()
        return assert_title

    def detail_buy(self):
        self.switch_window()
        title = self.detail_ele_buy()
        return title

    def play(self):
        self.driver.find_element(*self.locator_ele_play).click()
