#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :script_tencent.py
# @Time      :2021/5/9 10:37
# @author    :Harry

'''
1、腾讯课堂首页
2、分类选择：IT互联网-软件测试-自动化
3、列表页：搜索海德在线教育
4、类目选择：课程【IT互联网】-学习方向【软件测试】-分类【自动化测试】
        -知识点【selenium】-模式【录播】-排序【人气】
5、选择第一个课程
6、详情页：立即购买
7、登录页，选择QQ登录
8、登录后，查看任务；
'''
import time
from selenium import  webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
#首页
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://ke.qq.com/")
driver.implicitly_wait(30)

#分类选择
elem = driver.find_element(By.XPATH, '//*[@id="js_main_nav"]/div/div[1]/div[1]/a')
action = ActionChains(driver)
action.move_to_element(elem).perform()
time.sleep(3)

elem2 = driver.find_element(By.LINK_TEXT,'IT·互联网')
action.move_to_element(elem2).perform()
driver.find_element(By.LINK_TEXT,'自动化测试').click()
time.sleep(3)

#类表页
handles = driver.window_handles
driver.switch_to.window(handles[-1])

#搜索
driver.find_element(By.ID,'js_keyword').send_keys("海德在线教育")
driver.find_element(By.ID,'js_search').click()

#分类
driver.find_element(By.XPATH, '//*[@id="auto-test-1"]/div[1]/dl/dd[2]/a').click()
driver.find_element(By.XPATH,'//*[@id="auto-test-1"]/div[1]/dl/dd[9]/a/h2').click()

driver.find_element(By.XPATH,'//*[@id="auto-test-1"]/div/dl/dd[3]/a').click()
#知识点
driver.find_element(By.XPATH,'//*[@id="auto-test-1"]/div[2]/div[5]/dl/dd[5]/a/span[2]').click()
time.sleep(3)
#人气
driver.find_element(By.XPATH,'//*[@id="auto-test-4"]/a').click()

#课程
driver.find_element(By.XPATH,'/html/body/section[1]/div/div[5]/ul/li[1]/a/img').click()

time.sleep(3)
#立即购买
handles = driver.window_handles
driver.switch_to.window(handles[-1])
driver.find_element(By.XPATH,'//*[@id="js_btn_bar"]/span[1]/span/button/span[2]').click()

time.sleep(3)
driver.quit()