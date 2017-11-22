import cv2
import numpy as np
import matplotlib.pyplot as plt

img_man = cv2.imread('women.jpg',0) 
plt.subplot(121),plt.imshow(img_man,'gray'),plt.title('origial')
plt.xticks([]),plt.yticks([])
#--------------------------------
rows,cols = img_man.shape
mask = np.ones(img_man.shape,np.uint8)
mask[int(rows/2-30):int(rows/2+30),int(cols/2-30):int(cols/2+30)] = 0
#--------------------------------
f1 = np.fft.fft2(img_man)
f1shift = np.fft.fftshift(f1)
f1shift = f1shift*mask
f2shift = np.fft.ifftshift(f1shift)
img_new = np.fft.ifft2(f2shift)
img_new = np.abs(img_new)
img_new = (img_new-np.amin(img_new))/(np.amax(img_new)-np.amin(img_new))
plt.subplot(122),plt.imshow(img_new,'gray'),plt.title('Highpass')
plt.xticks([]),plt.yticks([])
plt.show()
