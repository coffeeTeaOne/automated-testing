#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :utils.py
# @Time      :2021/5/9 18:49
# @author    :Harry
from common.utils_mysql import DButils


def db_data_convert():
    sql = "select sname,ssex from student limit 0,5"
    result = DButils().searc_all(sql)

    print(result.keys(),result.values)


