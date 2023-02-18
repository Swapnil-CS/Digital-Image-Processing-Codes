import numpy as np
import cv2
import matplotlib.pyplot as plt

def normalizehist(hist):
    normhist=np.zeros(256,dtype="float")
    for i in range(256):
        normhist[i]=hist[i]/sum(hist)
    return normhist


def perforequalization(nhist):
    cumfreq=np.zeros(256,dtype="float")
    lookuptable=np.zeros(256,dtype="float")
    cumfreq[0]=nhist[0]
    for i in range(1,256):
        cumfreq[i]=cumfreq[i-1]+nhist[i]

    for i in range(256):
        lookuptable[i]=np.round(cumfreq[i]*255)
    return lookuptable

def findhistogram(img):
    h,w=img.shape
    hist=np.zeros(256,dtype='uint32')
    for i in range(h):
        for j in range(w):
            hist[img[i,j]]+=1
    return hist


img=cv2.imread('test.jpg',0)
h,w=img.shape
hist=findhistogram(img)


nhist=normalizehist(hist)


lookuptable=perforequalization(nhist)
eqim=img
for i in range(h):
    for j in range(w):
        eqim[i,j]=lookuptable[img[i,j]]
newhist=findhistogram(eqim)

original_img=cv2.imread('test.jpg',0)
fig = plt.figure(figsize=(18, 18))
pltX = 4
pltY = 1
fig.add_subplot(pltX, pltY, 1)
plt.imshow(cv2.cvtColor(original_img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title(" ORIGINAL IMAGE  ")

fig.add_subplot(pltX, pltY, 2)
plt.plot(hist)
plt.axis('on')
plt.title(" HISTOGRAM FOR ORIGINAL IMAGE ")
        
fig.add_subplot(pltX, pltY, 3)
plt.imshow(cv2.cvtColor(eqim, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title(" EQUALIZED IMAGE ")

fig.add_subplot(pltX, pltY, 4)
plt.plot(newhist)
plt.axis('on')
plt.title(" HISTOGRAM FOR EQUALIZED IMAGE ")

fig.show()
fig.waitforbuttonpress()


