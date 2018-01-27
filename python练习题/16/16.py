#!/usr/bin/python
import xlwt
a=[]
def wr_xls():
    ## read the file to cache
    cache = open("numbers.txt")
    file_wr = cache.read()
    cache.close()

    ## txt to list
    List_num = eval(file_wr)
    
    ## new xls
    work_book = xlwt.Workbook()
    xls_num = work_book.add_sheet(u'numbers')
    rows = 0
    for x in List_num:
        cols = 0
        for y in x:
            xls_num.write(rows,cols,y)
            cols += 1
        rows += 1
    work_book.save("numbers.xls")
        
if __name__ == '__main__':
    wr_xls()
