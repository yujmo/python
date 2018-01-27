#!/usr/bin/python2
import re
def words():
    jiao_huan = 0
    file_cache = open("filter_word")
    file_read = file_cache.readlines()
    file_cache.close()
    cache = raw_input("Please input a word:")
    if cache and cache !="q":
        for i in file_read:
            if re.findall(i[:-1],cache):
                print cache.replace(i[:-1],"*"*len(i[:-1]))
                jiao_huan = 1
        if jiao_huan == 0:
            print cache
        words()
    else:
        exit()
words()
