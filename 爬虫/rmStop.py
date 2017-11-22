from lib import *
import sys
if __name__ == "__main__":
    FileName = sys.argv[1:]
    for ee in FileName:
        res = RemoveStopWord(ee)
        newFileName = ee.split(".")[0]+"_new.txt"
        WriteFile(res,newFileName)
