#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_home.py
# @Time      :2021/5/10 18:11
# @author    :Harry

import pytest
from page.page_home import HomePage
from test_case.test_preset import TestPreSet


class TestHome(TestPreSet):

    @pytest.mark.parametrize('keywword', ['自动化测试'])
    def test_search(self,keywword):
        HomePage(self.driver).open("https://ke.qq.com/")
        HomePage(self.driver).search(keywword)
        title = self.driver.title
        self.logger.info(title)  # 输出日志
        self.logger.debug("------ 测试结束---- ")

        HomePage(self.driver).save_screen_pic(keywword)
        assert keywword in title

    @pytest.mark.skipif(1>0,condition="跳过用例执行")
    def test_login(self):
        HomePage(self.driver).open("https://ke.qq.com/")
        HomePage(self.driver).login()

    cate_one=['设计·创作', '电商·营销', 'IT·互联网', '升学·考研', '兴趣·生活','语言·留学']
    cate_two=['漫画绘本', '亚马逊', '性能测试', '专升本', '少儿编程','英语四六级']
    @pytest.mark.parametrize('cate_first, cate_second', zip(cate_one, cate_two))
    @pytest.mark.skip("跳过")
    def test_select_course(self,cate_first,cate_second):
        '''分类选择'''
        HomePage(self.driver).open("https://ke.qq.com/")
        HomePage(self.driver).select_category(cate_first, cate_second)
        HomePage(self.driver).switch_window()
        title = self.driver.title
        print(title)
        assert cate_second in title




if __name__ == '__main__':
    pytest.main(['-s', 'test_home.py'])