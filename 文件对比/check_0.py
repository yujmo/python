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
            execrise_file = result_file.replace("result","execrise")
            try:
                cache_result_file = open(result_file)
            except FileNotFoundError:
                break
            read_result_file = cache_result_file.readlines()
        #配置文件
            cache_execrise_file = open(execrise_file)
            read_execrise_file = cache_execrise_file.readlines()
        #----------------------------------------------------------------

            for j in read_result_file:
                cache_read_result_file = j.replace(" ","")#除去空格
                cache_re = re.findall(r,cache_read_result_file)#正则匹配
                if cache_re == []:#[],表示首字母没有匹配，即首字母不是#
                    if not cache_read_result_file.isspace():
                       #print(cache_read_result_file.rstrip('\n'))
                        print(cache_read_result_file)
#程序输出多余的空白。
#根据文件的特征，比如“=”、“：”等，将文件进行分开。
#利用根据文件所在的目录，根据hosts文件，进行判断主机名与IP的正确与否
#开始将输出结果写入到xls文件中。

#------------------------------------------------------------------------------

if __name__ == '__main__':
    get_result("result")
