#!/usr/bin/python2
import re
import urllib
def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html

def getImg(html):
    r = r'src="(.*?\.jpg)" bdwater='
    imglist = re.findall(r,html)
    x = 0
    for i in imglist:
        urllib.urlretrieve(i,'%s.jpg' %x)
        x += 1

html = getHtml("http://tieba.baidu.com/p/2166231880")
getImg(html)
