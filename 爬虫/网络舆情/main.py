from lib import *
import multiprocessing
import sys
if __name__ == '__main__':
    print("正在分析页面")
    webpage = GetHtml(sys.argv[1:][0])
    Links = GetUrlList(webpage)
    print("此网页上共有%d条链接记录,已生成目录文件。" % len(Links))
    fileName = sys.argv[1:][0].split(".")[1]     
    pool = multiprocessing.Pool(4)
    #pool = multiprocess.Pool(multiprocessing.cpu_count())
    for Link in Links:
        pool.apply_async(WebPagePrecess,(GetHtml(Link),fileName))
    input("共%d个页面，全部处理完成，按回车键退出。" % len(Links))
