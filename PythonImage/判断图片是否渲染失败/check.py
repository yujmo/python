import cv2
import argparse
from scipy.stats import mode

#这边主要是为了在命令行以-i或--image来指定要分析的图片（可以不用修改）
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to the image")
args = vars(ap.parse_args())

#读取图片，获取图片的长、宽等主要数据
im = cv2.imread(args["image"])

#（宽，长，colors不重要，不用管）
height,width,colors = im.shape

#用 （宽 乘以 长）得到这个图片一共有多少个像素点
sums = height * width

#将图片切分为B,G,R（顺序一定是B,G,R）
(B,G,R) = cv2.split(im)

#对众数进行数据的处理
#mode(t,axis=None)[0]可知B，G，R三色中每一色出现频率最高的值，比如R的0出现的次数最多
#mode(t,axis=None)[1]可知B，G，R三色中每一色出现频率最高的值，对应的次数
#用次数除以总的像素点，如果结果大于等于0.3，说明渲染失败。
dict_bgr = dict(B=B,G=G,R=R)
for key,value in dict_bgr.items():
    if mode(value,axis=None)[1]/sums >= 0.3:
        print("the picture\'s %s is error" % key)
