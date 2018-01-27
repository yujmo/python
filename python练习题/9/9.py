#!/usr/bin/python2
import re
def get_info():
    file_read = open("index.html")
    cache = file_read.read()
    r=r"src=\"?.*\"?"
    file_body = re.findall(r,cache)
    for i in file_body:
        print i

    file_read.close()

get_info()


