#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_preset.py
# @Time      :2021/5/10 9:40
# @author    :Harry
import time
from common.driver import chrome_driver
from common.utils_log import MyLog


class TestPreSet():
    def setup_method(self):
        print("测试执行开始")
        self.driver = chrome_driver()
        self.logger = MyLog('test', '../log/test.log')

    def teardown_method(self):
        print("测试执行结束")
        time.sleep(3)
        self.driver.quit()