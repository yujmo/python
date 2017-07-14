import urllib.request
import chardet
import os


def GetHtml(url):
        res = {}
        try:
                data = urllib.request.urlopen(url).read()
        except:
                res["data"] = "NULL"
                res["code"] = "NULL"
                return red
        code = chardet.detect(data)
        mode = code["encoding"]
        if "GB" in mode:
                mode = "GBK"
        res["data"] = data.decode(mode)
        res["code"] = mode
        return res


key = input("请输入URL.....")
FileName = input("请输入文件保存名     ")
print("正在抓取，请稍后.....")
tmp = "http://"
url = tmp + urllib.parse.quote(key)
d = GetHtml(url)
if d["data"] == "NULL" and d["code"] == "NULL":
        input("HTTP ERROR。按回车退出")
        os._exit(0)
out = open(FileName + ".html","wb")
out.write(d["data"].encode(d["code"]))
out.close()
input("抓取完成，按回车键退出。")
