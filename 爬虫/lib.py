from bs4 import BeautifulSoup
import requests
import re
import os
import jieba
import jieba.analyse

#---------------------------------------------------------------------------------------------------------
def GetHtml(address):
    webdata = requests.get(address)
    webdata.encoding = webdata.apparent_encoding
    webpage = BeautifulSoup(webdata.text,"lxml")
    return webpage
#---------------------------------------------------------------------------------------------------------
def ReadFile(rfile):
    with open(rfile) as rf:
        return rf.readlines()
#---------------------------------------------------------------------------------------------------------
def WriteFile(res,wfile):
    with open(wfile,'a') as wf:
        wf.writelines(res)
#---------------------------------------------------------------------------------------------------------
def GetUrlList(webpage):
    LinkTag = webpage.find_all('a',href=re.compile("[http|https]"))
    LinkListCache = ([re.findall(r"href=\"https?.+",str(Link)) for Link in LinkTag])
    return [t[0].split("\"")[1] for t in LinkListCache if t]
#---------------------------------------------------------------------------------------------------------
def WebPagePrecess(webpage,fileName):
    cache = webpage.get_text()
    punct = ''':!),.:;?]}¢'"・、。〉》」』】〕〗〞︰︱︳﹐､﹒
    ﹔﹕﹖﹗﹚﹜﹞！），．：；？｜｝︴︶︸︺︼︾﹀﹂﹄﹏､～￠ 
    々‖•·ˇˉ―--′’”([{£¥'"‵〈《「『【〔〖（［｛￡￥〝︵︷︹︻  
    ︽︿﹁﹃﹙﹛﹝（｛“‘-—_…|!@#$%^&*()_+\/|><=——_~╋      
    ` ×©\n\r┊\b　 丨●abcdefghijklmnopqrstuvwxyz0123456789
    ABCDEFGHIJKLMNOPQRSTUVWXYZ'''
    
    cache_res = [x for x in cache if x not in punct]
    res = "".join(res)
    k = jieba.cut(res)
    word =  "\n".join(k)
    #return word
    WriteFile(word,fileName + ".txt")
#---------------------------------------------------------------------------------------------------------
def RemoveStopWord(FileName):
    cacheMu = ReadFile("停用词库.txt")
    stopWord = set(cacheMu)
    cacheFile = ReadFile(FileName)
    cacheWord = set(cacheFile)
    return cacheWord - stopWord
#---------------------------------------------------------------------------------------------------------
def FileOpen(FileName):
    with open(FileName) as rf:
        f = rf.read()
    return f
#--------------------------------------------------------------------------------------------------------
def GetKeywords(Data,topK=50):
    jieba.enable_parallel(4)    
    return  jieba.analyse.extract_tags(Data,topK=topK)
#--------------------------------------------------------------------------------------------------------
