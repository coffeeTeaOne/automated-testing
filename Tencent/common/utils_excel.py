#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :utils_excel.py
# @Time      :2021/5/9 17:18
# @author    :Harry
import xlrd
import xlwt

def excel_write(filename):
   wb = xlwt.Workbook()  #实例化工作薄
   sheet = wb.add_sheet(sheetname='学生信息') #添加sheet
   #写入内容
   sheet.write(0, 0, 'name')
   sheet.write(0, 1, 'sex')
   sheet.write(0, 2, 'age')
   sheet.write(0, 3, 'class')

   sheet.write(1, 0, 'zhangsan')
   sheet.write(1, 1, '男')
   sheet.write(1, 2, '18')
   sheet.write(1, 3, '21012')
   print("保存成功")
   wb.save(filename)

def excel_read(filename):
   wb = xlrd.open_workbook(filename)
   sheet_names = wb.sheet_names()  # 获取sheet的名称
   print(sheet_names)

   #sheet 读取
   sheet = wb.sheet_by_name('学生信息')

   rows = sheet.nrows
   cols = sheet.ncols
   print("共有{}行，{}列".format(rows,cols))

   # 读取行内容
   row_values = sheet.row_values(0)   #获取第一行内容
   print("第一行内容{}".format(row_values))

   col_values=sheet.col_values(1)  # 获取第二例内容
   print("第2列内容{}".format(col_values))

   cell_value = sheet.cell(1,2)
   print(cell_value)




filename = 'user.xlsx'
excel_write(filename)
excel_read(filename)






