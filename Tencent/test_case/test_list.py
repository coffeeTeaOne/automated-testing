#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_list.py
# @Time      :2021/5/10 15:56
# @author    :Harry
import pytest
from page.page_list import ListPage
from test_case.test_preset import TestPreSet

class TestList(TestPreSet):

    menu_course = ['设计·创作', '电商·营销', 'IT·互联网', '升学·考研', '兴趣·生活', '语言·留学']
    menu_learn = ['绘画创作', '跨境电商', '软件测试', '大学','母婴亲子', '英语']
    menu_cate = ['漫画绘本', '亚马逊', '性能测试', '专升本', '少儿编程', '英语四六级']
    @pytest.mark.parametrize('course,learn,category', zip(menu_course, menu_learn,menu_cate))
    @pytest.mark.skip('跳过用例')
    def test_menu(self, course, learn, category):
        ListPage(self.driver).open('https://ke.qq.com/course/list')
        ListPage(self.driver).sort_by(course, learn, category)

    @pytest.mark.skipif(1>0,"跳过用例")
    def test_order(self):
        ListPage(self.driver).open('https://ke.qq.com/course/list')
        ListPage(self.driver).order_by('免费课', '人气', '￥1-99')

    @pytest.mark.skipif(1 > 0, "跳过用例")
    def test_sort_and_order(self):
        ListPage(self.driver).open('https://ke.qq.com/course/list')
        ListPage(self.driver).sort_by('电商·营销', '跨境电商', '亚马逊')
        ListPage(self.driver).order_by('付费课', '价格', '￥500-999')

    # @pytest.mark.skipif(1 < 0, "跳过用例")
    def test_choose_course(self):
        try:
            ListPage(self.driver).open('https://ke.qq.com/course/list')
            ListPage(self.driver).order_by('付费课', '价格', '￥500-999')
            ListPage(self.driver).elem_course_name()
        except Exception as e:
            self.logger.error(e)
        finally:
            self.logger.debug('----选课完成------')


if __name__ == '__main__':
    pytest.main(['test_list.py'])