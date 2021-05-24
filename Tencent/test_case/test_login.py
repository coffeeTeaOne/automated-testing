#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :test_login.py
# @Time      :2021/5/10 9:39
# @author    :Harry
import pytest

from page.page_login import LoginPage
from test_case.test_preset import TestPreSet


class TestLogin(TestPreSet):
    def test_login(self):
        LoginPage(self.driver).login()

if __name__ == '__main__':
    pytest.main(['-s', 'test_login.py'])