#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :utils.py
# @Time      :2021/5/23 17:30
# @author    :Harry
import os

from ITFAuto.config.setting import DATA_PATH,TEMPLATE_PATH, CASE_PATH



def create_case():
    """从模板中读取内容，生成新的testcase用例"""
    # 获取所有接口名称
    file_list = os.listdir(DATA_PATH)  # 获取目录下的所有文件
    for file in file_list:
        if file.endswith('.yaml') or file.endswith('.yml'):  # 判断yaml
            file = file.replace('.yaml', '').replace('.yml', '')
            print(file)
            class_name = file.capitalize()  # 驼峰命名 类名首字母大写
            file_name = file.lower()  # 转换全小写字母
            case_name = file_name
            #读取模板文件内容，并替换变量
            with open(TEMPLATE_PATH, 'r', encoding='utf-8') as f:
                content = f.read() % {
                    'class_name': class_name,
                    'file_name': file_name,
                    'case_name': case_name
                }

            # 写入内容到case 文件中
            filename = os.path.join(CASE_PATH, 'test_'+file_name+'.py')
            with open(filename, 'w+', encoding='utf-8') as f:
                f.write(content)

create_case()
