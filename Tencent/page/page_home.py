#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :page_home.py
# @Time      :2021/5/9 11:36
# @author    :Harry
import time
from selenium.webdriver.common.by import By
from page.page_base import BasePage


class HomePage(BasePage):

    #定位器
    locator_cate_nav = (By.XPATH, '//*[@id="js_main_nav"]/div/div[1]/div[1]/a')  # 顶部导航-分类菜单
    locator_login_nav = (By.XPATH, '//*[@id="js_login"]')                        # 顶部导航-登录

    locator_login_frame = (By.XPATH, '/html/body/div[2]/section/div[2]/div/div/iframe')  # 登录按钮
    locator_login_user = (By.XPATH, '//*[@id="qlogin_list"]/a')  # 登录弹框用户头像

    locator_search_keyword = (By.ID, 'js_keyword')  # 搜索输入框
    locator_search_btn = (By.ID, 'js_search111')  # 搜索按钮

    def ele_search_keyword(self,keyword):
        try:
            self.driver.find_element(*self.locator_search_keyword).send_keys(keyword)
        except Exception as e:
            self.logger.error(e)

    def ele_search_btn(self):
        try:
            self.driver.find_element(*self.locator_search_btn).click()
        except Exception as e:
            self.logger.error(e)

    def search(self,keyword):
        '''搜索'''
        self.logger.info('----- 搜索开始 --------')
        try:
            self.ele_search_keyword(keyword)
            self.ele_search_btn()
        except Exception as e:
            self.logger.error(e)
        finally:
            self.logger.info("-----搜索结束------")

    def elem_login_btn(self):
        '''导航登录按钮'''
        self.driver.find_element(*self.locator_login_nav).click()
        time.sleep(3)

    def elem_login_frame(self):
        '''登录弹框frame'''
        iframe = self.driver.find_element(*self.locator_login_frame)
        return iframe

    def elem_login_user(self):
        self.driver.find_element(*self.locator_login_user).click()
        print("登录成功")
        time.sleep(3)

    def login(self):
        self.elem_login_btn()
        # 进入frame
        self.switch_frame_enter(self.elem_login_frame())
        # 登录
        self.elem_login_user()
        # 退出frame
        self.switch_frame_quit()


    def elem_cate_menu(self):
        '''分类菜单'''
        elem = self.driver.find_element(*self.locator_cate_nav)
        return elem

    def elem_cate_first(self, cate_first):
        '''一级分类'''
        elem2 = self.driver.find_element(By.LINK_TEXT, cate_first)
        return elem2

    def elem_cate_second(self, cate_second):
        '''二级分类'''
        self.driver.find_element(By.LINK_TEXT, cate_second).click()

    def select_category(self, cate_first, cate_second):
        '''分类选择'''
        # 悬浮选择顶部导航【分类】
        self.move_to_menu(self.elem_cate_menu())
        time.sleep(2)
        # 悬浮选择分类中的“一级导航类目”
        self.move_to_menu(self.elem_cate_first(cate_first))
        time.sleep(2)
        # 选择一级分类下的二级分类
        self.elem_cate_second(cate_second)
        time.sleep(2)

