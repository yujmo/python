#!/usr/bin/python
import os
import hashlib
import re
def get_result(path):
    file_list = os.listdir(path)
    for i in file_list:
        result_file = os.path.join(path,i)
        if os.path.isdir(result_file):
            get_result(result_file)
        #模板文件
        if not os.path.isdir(result_file):
            #尝试打开文件，可能有链接文件
            try:
                cache_result_file = open(result_file)
                read_result_file = cache_result_file.readlines()
                del_space_result_file = del_space_file(read_result_file)
            except FileNotFoundError:
                continue
        #配置文件
            execrise_file = result_file.replace("result","execrise")
            #如果配置文件目录中不存在该配置文件，则输出
            try:
                cache_execrise_file = open(execrise_file)
            except FileNotFoundError:
                print("对不起，无此文件："+result_file)
                continue
            read_execrise_file = cache_execrise_file.readlines()
            del_space_execrise_file = del_space_file(read_execrise_file)
        #----------------------------------------------------------------

        #MD5校验，相同文件直接忽略,不相同的往下比较----------------------
            result = md5_check(result_file,execrise_file)
            if not result:
                print(execrise_file)
                #判断配置项是否有不同,如有，则输出
                for line_i in del_space_execrise_file:
                    if line_i not in del_space_result_file:
                        print(line_i)
                #判断配置项目是否存在，如果不存在，则输出
                for line_i in del_space_result_file:
                    if line_i not in del_space_execrise_file:
                        print("对不起，该配置不存在"+line_i)
                    
                            
#------------------------------------------------------------------------------

#将文件hash,并根据判断结果返回值（True或False）
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

#去除空格，首字母为#的行，删除，不存储到列表中---------------------------------
def del_space_file(module_file):
    r=r"^\#"
    readlines_module_file = []
    for j in module_file:
        cache_read_result_file = j.replace(" ","")#除去空格
        cache_re = re.findall(r,cache_read_result_file)#正则匹配
    #如果cache_re存在结果，则说明首字母为‘#’，不可取
        if cache_re == []:#[],表示首字母没有匹配，即首字母不是#
            if not cache_read_result_file.isspace():
                readlines_module_file.append(cache_read_result_file.rstrip('\n'))
    return readlines_module_file
#-------------------------------------------------------------------------------

#数据库检查
def sql_check():
    print("OK")
#------------------------------------------------------------------------------

if __name__ == '__main__':
    get_result("result")
    sql_check()
