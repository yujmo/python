#-*- coding: UTF-8 -*-
"""
1.读取/root/depth/下的深度图像，对图像进行切割。
2.对图像实现切割之后，再使用MatLab对图像进行去除背景。

###: 原始图像/root/depth/
###: 切割后的图像/root/results

height: 424
width:  512
320 240
"""
import numpy as np
import os
import cv2
import scipy.io as scio
import matplotlib.image as mpimg

h_min = 40 #40-68
h_max = 70
f_min = 60 #62-68
f_max = 70

def eachFile(filepath):
    return [os.path.join('%s%s' % (filepath,allDir)) for allDir in os.listdir(filepath)]

def bgAlt(value):
    if (value < h_min) or (value > h_max):
        return 0
    else:
        value = float(value-h_min)*255/(h_max-h_min);
        return np.uint8(value)

def cutPicture(picture_read_path):
    image = cv2.imread(picture_read_path,0)[0:380,56:466] #height,width
    height,width = image.shape
    im_mat = np.zeros((height,width),dtype=np.uint8)
    #[im_mat[x][y]=bgAlt(image[x][y]) for x in range(0,height) for y in range(0,width)]
    for x in range(0,height):
        for y in range(0,width):
            im_mat[x][y] = bgAlt(image[x][y])

    scio.savemat(picture_read_path.replace("depth","test_mat").replace("png","mat"),{'dict':im_mat})
    #scio.savemat(picture_read_path.replace("depth","results").replace("png","mat"),{'dict':im_mat})

if __name__ == '__main__':
    depth_pictures = eachFile('/root/depth/')
    [cutPicture(x) for x in depth_pictures]
    #cutPicture(depth_pictures[0])
