#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :page_list.py
# @Time      :2021/5/9 11:36
# @author    :Harry
import time
from selenium.webdriver.common.by import By
from page.page_base import BasePage

class ListPage(BasePage):

    #定位器
    locator_course_name =(By.XPATH, '//ul[@class="course-card-list"]/li[1]/a/img') #课程

    #筛选
    def ele_sort_menu_course(self, course):
        self.driver.find_element(By.LINK_TEXT, course).click()
        time.sleep(1)

    def ele_sort_menu_learn(self, learn):
        self.driver.find_element(By.LINK_TEXT, learn).click()
        time.sleep(1)

    def ele_sort_menu_category(self, category):
        self.driver.find_element(By.LINK_TEXT, category).click()
        time.sleep(1)
    #排序
    def ele_order_by_free(self, free):
        '''课程类型：免费课，付费课'''
        self.driver.find_element(By.LINK_TEXT, free).click()

    def ele_order_by_sort(self, sort):
        '''综合排序：好评率，人气，价格'''
        self.driver.find_element(By.LINK_TEXT, sort).click()

    def ele_order_by_price(self, price):
        '''课程价格:￥1-99'''
        elem = self.driver.find_element(By.CLASS_NAME, 'dropdown-toggle')
        self.move_to_menu(elem)
        time.sleep(1)
        self.driver.find_element(By.LINK_TEXT, price).click()

    #################################################################
    def order_by(self, free, sort, price):
        '''排序'''
        self.ele_order_by_free(free)
        self.ele_order_by_sort(sort)
        self.ele_order_by_price(price)

    def sort_by(self,course,learn,category):
        '''筛选过滤'''
        self.ele_sort_menu_course(course)
        self.ele_sort_menu_learn(learn)
        self.ele_sort_menu_category(category)

    def elem_course_name(self):
        '''课程内容选择'''
        self.driver.find_element(*self.locator_course_name).click()

    def choose_course(self):
        self.elem_course_name()