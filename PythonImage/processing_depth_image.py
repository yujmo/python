#-*- coding: UTF-8 -*-
"""
1.读取/root/depth/下的深度图像，对图像进行切割。
2.对图像实现切割之后，再使用MatLab对图像进行去除背景。

###: 原始图像/root/depth/
###: 切割后的图像/root/results

height: 424
width:  512
"""

import os
import cv2

def eachFile(filepath):
    return [os.path.join('%s%s' % (filepath,allDir)) for allDir in os.listdir(filepath)]

def cutPicture(picture_read_path):
    image = cv2.imread(picture_read_path)[0:385,150:475] #height,width
    cv2.imwrite(picture_read_path.replace("depth","results"),image)

if __name__ == '__main__':
    depth_pictures = eachFile('/root/depth/')
    [cutPicture(x) for x in depth_pictures]
