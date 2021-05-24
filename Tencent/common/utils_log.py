#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :utils_log.py
# @Time      :2021/5/16 14:35
# @author    :Harry

import logging  # 引入logging模块
import os
import time

class MyLog(logging.Logger):
    def __init__(self, name, file_name=None):
        self.name = name
        self.log_name = file_name
        self.level = logging.INFO
        self.fmt = "%(asctime)s, Module:%(name)s - [File:%(filename)s - Lines:%(lineno)d] - %(levelname)s ：%(message)s"
        self.f_handle = logging.FileHandler(filename=self.log_name,encoding='utf-8')
        self.s_handle = logging.StreamHandler()
        self.formatter = logging.Formatter(self.fmt)
        super().__init__(name=self.name)

        if self.log_name is not None:
            self.f_handle.setFormatter(self.formatter)
            self.addHandler(self.f_handle)
        else:
            self.s_handle.setFormatter(self.formatter)
            self.addHandler(self.s_handle)

# if __name__ == '__main__':
#     logger = MyLog('gouwuch', '../log/aaa.log')
#     logger.info("---hhhhhhh----")
#     logger.debug('----dddddddddddddddddddd')


# logging.basicConfig(level=logging.ERROR)

# my_log = logging.getLogger()
# my_log = logging.Logger('hello')
# my_log.setLevel(level=logging.INFO)  #设置日志级别
#
# # # 文件句柄对象
# logfile = 'log-2021-05-17.log'
# f_handle = logging.FileHandler(filename=logfile, mode='a', encoding='utf-8')
# #
# # #设置日志格式
# formater = "%(asctime)s,[%(filename)s - Lines:%(lineno)d] - %(levelname)s ：%(message)s"
# formatter = logging.Formatter(formater)
# f_handle.setFormatter(formatter)
#
# my_log.addHandler(f_handle)      # 输出日志到文件
# #
# # # 输出到控制台
# # s_handle = logging.StreamHandler()   #控制台句柄对象
# # s_handle.setFormatter(formatter)
# # my_log.addHandler(s_handle)
#
#
# my_log.debug('---debug msg --- ')
# my_log.info('--- info msg ---')
# my_log.warning('---- warning msg')
# my_log.error('---- error msg ---')
# my_log.critical('----critical msg----')


import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)  # 设定日志级别
#创建文件Handler
logpath= os.path.join(os.path.dirname(os.getcwd()),'log')
filename = time.strftime('%Y-%m-%d', time.localtime())+'.log'
logfile = os.path.join(logpath, filename)

# logfile='log-2021-05-17.log'
f_handle = logging.FileHandler(logfile, mode='a',encoding='utf-8')

#日志格式设置
format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s'
#创建日志格式对象
formatter = logging.Formatter(format)
f_handle.setFormatter(formatter)
#日志写入文件
logger.addHandler(f_handle)

#日志输出到控制台
s_handler = logging.StreamHandler()
s_handler.setLevel(logging.WARNING)
s_handler.setFormatter(formatter)
logger.addHandler(s_handler)



#日志打印
logger.debug('---debug msg --- ')
logger.info('--- info msg ---')
logger.warning('---- warning msg')
logger.error('---- error msg ---')
logger.critical('----critical msg----')

