#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_flow.py
# @Time      :2021/5/16 10:55
# @author    :Harry
import pytest
from page.page_detail import DetailPage
from page.page_home import HomePage
from page.page_list import ListPage
from test_case.test_preset import TestPreSet


class TestFlow(TestPreSet):
    def test_flow_1(self):
        '''
        1、首页登录
        2、首页搜索
        3、列表选课
        4、详情页播放视频学习课程
        :return:
        '''
        HomePage(self.driver).open('https://ke.qq.com/')
        HomePage(self.driver).login()
        HomePage(self.driver).search('自动化测试')
        ListPage(self.driver).choose_course()

        ListPage(self.driver).switch_window()
        print(self.driver.title)
        DetailPage(self.driver).switch_frame_enter('js-study-video')
        #播放视频
        DetailPage(self.driver).play()



    def test_flow_2(self):
        pass

    def test_flow_3(self):
        pass
if __name__ == '__main__':
    pytest.main(['-s','test_flow.py'])