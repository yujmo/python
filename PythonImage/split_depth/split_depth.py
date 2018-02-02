import os
import time
import shutil
split_depth = lambda strs: strs[2:-3].split('],[')

if __name__ == '__main__':
    with open('depth.txt') as fp:
        content  = list(fp.readlines())
    depth_files = [content[x:x+2] for x in range(0,len(content),2)]
    for labels,dirs in depth_files:
        os.chdir(labels.strip("\n")+"_depth")
        files_ints = [int(ef.split(".")[0]) for ef in os.listdir(".")]
        for x in split_depth(dirs):
            dir_f,dir_b = x.split(",")
            os.makedirs("../tmp/"+labels.strip("\n")+"/"+dir_f+"_"+dir_b)
            for ee in files_ints:
                if ee >= int(dir_f) and ee <= int(dir_b):
                    shutil.copy(str(ee)+".png","../tmp/"+labels.strip("\n")+"/"+dir_f+"_"+dir_b)
                    files_ints.remove(ee)
        os.chdir("..")
