#!/usr/bin/python2
import re
def get_info():
    file_read = open("index.html")
    cache = file_read.read()
    r=r"<body[.\s\S]*</body>"
    file_body = re.findall(r,cache)
    print file_body
    file_read.close()

get_info()


