#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :utils_mysql.py
# @Time      :2021/5/9 17:53
# @author    :Harry
import pymysql

class DButils():
    def __init__(self):
        #建立连接
        self.conn = pymysql.connect(host='localhost',
                        port=3306,
                        user='root',
                        password='',
                        db='hd45',
                        charset='utf8',
                        cursorclass=pymysql.cursors.DictCursor
                                    )
        print("连接成功")
        self.cursor = self.conn.cursor() #创建游标

    def close(self):
        self.cursor.close()
        self.conn.close()

    def searc_one(self,sql):
        #操作
        # sql = 'SELECT * FROM student LIMIT 0 , 10'
        self.cursor.execute(sql)
        result = self.cursor.fetchone()
        print(result)
        self.close()
        return result

    def searc_all(self,sql):
        #操作
        # sql = 'SELECT * FROM student LIMIT 0 , 10'
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        print(results)
        self.close()
        return results

    def add(self,sql):
        # 提交：增、删、改
        # sql= "insert into student values('998','董同学','男','2020-11-11','98021')"
        self.cursor.execute(sql)
        self.conn.commit()  #提交
        self.close()

    def update(self):
        pass

    def delete(self):
        pass
