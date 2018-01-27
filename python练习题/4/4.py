#!/usr/bin/python2
def get_info():
    t = {}
    file_read = open("result")
    cache = file_read.read().split(" ")
    for i in cache:
        if i != "\n":
            if not  t.get(i,0):
                t[i]=1
            else:
                x = t[i]
                t[i] = x + 1
    file_read.close()
    print t

get_info()


