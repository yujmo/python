#!/usr/bin/python
import xlwt
a=[]
def wr_xls():
    cache = open("city.txt")
    file_wr = cache.read()
    cache.close()
    work_book = xlwt.Workbook()
    student = work_book.add_sheet(u'city')
    item = eval(file_wr)
    rows = 0
    for key,value in item.items():
        a.append(key)
    a.sort()
    for x in a:
        cols = 0
        student.write(rows,cols,x)
        cols += 1
        student.write(rows,cols,item[x])
        rows += 1
    work_book.save("city.xls")
        
if __name__ == '__main__':
    wr_xls()
