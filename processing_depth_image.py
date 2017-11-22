#-*- coding: UTF-8 -*-
"""
1.读取/root/depth/下的深度图像，对图像进行切割。
2.对图像实现切割之后，再使用MatLab对图像进行去除背景。

###: 原始图像/root/depth/
###: 切割后的图像/root/results
"""

import os
import cv2

def eachFile(filepath):
    return [os.path.join('%s%s' % (filepath,allDir)) for allDir in os.listdir(filepath)]

eachFile('/root/depth/')
