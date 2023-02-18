import numpy as np
import cv2
import matplotlib.pyplot as plt

img=cv2.imread('test.jpg',0)
hist=np.zeros(256)
h,w=img.shape
for i in range(h):
    for j in range(w):
        hist[img[i,j]]+=1

fig, axs=plt.subplots(1,2)
x=np.arange(0,256,1)
axs[0].plot(x,hist)
axs[0].set_xlabel("X")
axs[0].set_ylabel("y")
axs[0].set_title("histogram")
axs[1].imshow(img,cmap="gray")
axs[1].set_title('GRAY IMAGE')
plt.show()
