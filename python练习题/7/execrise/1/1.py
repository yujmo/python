#!/usr/bin/python2
import random

def get_code():
    chars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    file_result = open("result","w+")
    for i in range(200):
        cache_str=""
        for x in range(20):
            cache_str = cache_str + chars[random.randint(0,len(chars)-1)]
        file_result.write(cache_str+"\n")
    file_result.flush()
    file_result.close()

get_code()
