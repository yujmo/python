#!/usr/bin/python
import os
import hashlib
import re
r=r"^\#"
def get_result(path):
    file_list = os.listdir(path)
    for i in file_list:
        result_file = os.path.join(path,i)
        if os.path.isdir(result_file):
            get_result(result_file)
        #读取文件（Try）-----------------------------------------------------
        #模板文件
        if not os.path.isdir(result_file):
#           execrise_file = result_file.replace("result","execrise")
            try:
                os.path.isfile(result_file)
            except FileNotFoundError:
                break
            cache_result_file = open(result_file)
            read_result_file = cache_result_file.readlines()
        #配置文件
            cache_execrise_file = open(execrise_file)
            read_execrise_file = cache_execrise_file.readlines()
        #----------------------------------------------------------------

        #MD5校验，相同文件直接忽略,--------------------------------------
            result = md5_check(result_file,execrise_file)
            if not result:
        #检查去空格后首字母是否为'#'-------------------------------------

#------------------------------------------------------------------------------
#将文件hash,并根据判断结果返回值（1|0）
def md5_check(result_file,execrise_file):
    #打开模板文件，将文件hash
    cache_result_file = open(result_file)
    read_result_file = cache_result_file.read()
    md5_result_file = read_result_file.encode("utf-8")
    m1 = hashlib.md5(md5_result_file)
    #打开配置文件，将文件hash
    cache_execrise_file = open(execrise_file)
    read_execrise_file = cache_execrise_file.read()
    md5_execrise_file = read_execrise_file.encode("utf-8")
    m2 = hashlib.md5(md5_execrise_file)
    #关闭文件
    cache_result_file.close()
    cache_execrise_file.close()
    #如果文件hash相同，则返回1
    if m1.hexdigest()==m2.hexdigest():
        return 1
    #否则返回0
    return 0
#------------------------------------------------------------------------------

#去除空格，列表方式存储--------------------------------------------------------
def del_space_file(module_file):
    readlines_module_file = []
    for j in read_result_file:
        cache_read_result_file = j.replace(" ","")#除去空格
        cache_re = re.findall(r,cache_read_result_file)#正则匹配
    #如果cache_re存在结果，则说明首字母为‘#’，不可取
        if cache_re == []:#[],表示首字母没有匹配，即首字母不是#
            if not cache_read_result_file.isspace():
                readlines_module_file.append(cache_read_result_file.rstrip('\n'))
    return readlines_module_file
#-------------------------------------------------------------------------------

if __name__ == '__main__':
    get_result("result")

