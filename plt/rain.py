import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import animation
import os
#确定ffmpeg.exe的位置，试过加在环境变量里但依然提示找不到MovieWriter，最后这个方法解决了，在Python2.7版本路径名前面要声明编码是unicode的，而在Python3中有无均可，这是2.X和3.x版本的一个编码方面的区别
plt.rcParams['animation.ffmpeg_path'] = u"D:\\Applications\\ffmpeg-20170503-a75ef15-win64-static\\bin\\ffmpeg.exe"
#这里改变当前工作路径，方便下面保存文件的时候自动保存到该路径下面
os.chdir("d:\\Files\\python\\matplotlib") 
# No toolbar
matplotlib.rcParams['toolbar'] = 'None'
# New figure with white background
fig = plt.figure(figsize=(6,6), facecolor='white')
# New axis over the whole figureand a 1:1 aspect ratio
# ax = fig.add_axes([0,0,1,1], frameon=False, aspect=1)
ax = fig.add_axes([0.005,0.005,0.990,0.990], frameon=True, aspect=1)
# Number of ring
n = 50
size_min = 50
size_max = 50*50
# Ring position ，圆环位置，范围在[0,1]之间
P = np.random.uniform(0,1,(n,2))
# Ring colors环的颜色
C = np.ones((n,4)) * (0,1,0,1)
#C = np.ones((n,3)) * (1,0,1)
# Alpha color channel goes from 0 (transparent) to 1 (opaque)
# 透明度，数值在[0,1]之间
C[:,2] = np.linspace(0,1,n)
# Ring sizes环的大小，范围在[50,2500]
S = np.linspace(size_min, size_max, n)
# Scatter plot
# 散点图绘制
scat = ax.scatter(P[:,0], P[:,1], s=S, lw = 0.5,
         edgecolors = C, facecolors='None')
# Ensure limits are [0,1] and remove ticks
#保证x,y的范围在[0,1]之间,移除坐标轴标记
ax.set_xlim(0,1), ax.set_xticks([])
ax.set_ylim(0,1), ax.set_yticks([])
def update(frame):
  global P, C, S
  # Every ring is made more transparent每个环变得更透明
  C[:,3] = np.maximum(0, C[:,3] - 1.0/n)
  # Each ring is made larger每个环都比原来的大
  S += (size_max - size_min) / n
  # Reset ring specific ring (relative to frame number)
  i = frame % 50 
  P[i] = np.random.uniform(0,1,2) # P[i] = P[i,:],同时改变了x,y两个位置的值
  S[i] = size_min #从最小的形状开始
  C[i,3] = 1   #设置透明度为1 
  # Update scatter object
  # 更新scatter绘图对象的属性，例如edgecolors,sizes,offsets等
  scat.set_edgecolors(C) #设置边缘颜色
  scat.set_sizes(S)    #设置大小
  scat.set_offsets(P)   #设置偏置
  return scat,
animate = FuncAnimation(fig, update, frames = 300,interval=70)#interval是每隔70毫秒更新一次，可以查看help
FFwriter = animation.FFMpegWriter(fps=20)  #frame per second帧每秒
animate.save('rain.mp4', writer=FFwriter,dpi=360)#设置分辨率
plt.show()
