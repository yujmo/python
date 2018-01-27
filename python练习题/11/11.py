#!/usr/bin/python2
import re
def words():
    file_cache = open("filter_word")
    file_read = file_cache.readlines()
    file_cache.close()
    cache = raw_input("Please input a word:")
    if cache and cache !="q":
        for i in file_read:
            if cache == i[:-1]:
                print "freedom"
        words()
    else:
        exit()
words()
