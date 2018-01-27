#!/usr/bin/python2
import os
def get_info():
    path = "txt"
    file_list = os.listdir(path)
    all_file=[]
    for i in file_list:
        all_file.append(os.path.join(path,i))
    return all_file

def get_word(path_file):
    a = []
    for i in path_file:
        file_read = open(i)
        cache = file_read.read().split(" ")
        t = {}
        for i in cache:
            if i != "\n":
                if not t.get(i,0):
                    t[i]=1
                else:
                    t[i] = t[i] + 1
        pp = 0
        for x,y in t.items():
            if y  >= pp:
                pp = y
        for x,y in t.items():
            if y == pp:
                if x not in a:
                    a.append(x)
        file_read.close()
    print a

path_file=get_info()
get_word(path_file)
