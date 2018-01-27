#!/usr/bin/python2
import os
import re
a=[]
tt=[]
def get_info(path):
    all_file=[]
    file_list = os.listdir(path)
    for i in file_list:
        file_name=os.path.join(path,i)
        if os.path.isdir(file_name):
            get_info(file_name)
        if not os.path.isdir(file_name):
            all_file.append(file_name)
    a.append(all_file)

def get_file():
    aaa=bbb=ccc=count=0
    count = 0
    r = r".*\.py$"
    for i in a:
        for x in i:
            xxxx = re.findall(r,x)
            if xxxx:
                count = count + 1 
                for j in xxxx:
                    cache = open(j)
                    file_read = cache.readlines()
                    for ttt in file_read:
                        if ttt == "\n":
                            aaa = aaa + 1
                        else:
                            if re.findall("^#",ttt):
                                bbb = bbb + 1
                            else:
                                ccc = ccc + 1
                    cache.close()
    print "Enter=%d" % aaa
    print "#=%d" % bbb
    print "lines=%d" % ccc 
    print "count=%d" % count

get_info("execrise")
get_file()
