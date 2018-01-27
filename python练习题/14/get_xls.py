#!/usr/bin/python
#coding:utf-8
import xlrd
def read_xls():
    workbook = xlrd.open_workbook("test.xls")
    sheet1 = workbook.sheet_by_index(0)
    sheet2 = workbook.sheet_by_name("xyz")
    print ("*********************************")
    print (sheet2.name)
    print (sheet2.nrows)
    print (sheet2.ncols)
    print ("*********************************")
    print (sheet1.row_values(3))
    print (sheet1.col_values(3))
    print ("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print (sheet1.cell(1,0).value)
    print (sheet1.cell_value(1,0))
    print (sheet1.row(1)[0].value)
    print ("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&")
    print (sheet2.cell(0,0).ctype)

if __name__ == '__main__':
    read_xls()
