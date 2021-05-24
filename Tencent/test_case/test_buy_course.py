#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_buy_course.py
# @Time      :2021/5/9 11:18
# @author    :Harry
import pytest
import time
from common.driver import chrome_driver
from page.page_detail import DetailPage
from page.page_home import HomePage
from page.page_list import ListPage
from test_case.test_preset import TestPreSet


class TestBuyCourse(TestPreSet):

    # @pytest.mark.parametrize('keyword', ['海德在线教育'])
    # @pytest.mark.skip("跳过")
    def test_buy_course(self):
        # 首页访问分类
        HomePage(self.driver).open('https://ke.qq.com/')
        HomePage(self.driver).select_category('IT·互联网','自动化测试')

        #进入列表页面
        ListPage(self.driver).switch_window()
        ListPage(self.driver).order_by('免费课', '好评率', '￥100-499')
        time.sleep(1)
        ListPage(self.driver).elem_course_name()

        # 详情页
        DetailPage(self.driver).switch_window()
        title = DetailPage(self.driver).detail_buy()
        print(title)
        # assert keyword in title

if __name__ == '__main__':
    pytest.main(['-s', 'test_buy_course.py'])