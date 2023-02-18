import cv2
import numpy as np
import matplotlib.pyplot as plt

def samepadding(img):
    h,w=img.shape
    newimage=np.zeros([h+2,w+2]).astype(np.uint8)
    for i in range (h):
        for j in range(w):
            newimage[i+1,j+1]=img[i,j]
    newimage[0,0]=newimage[1,1]
    newimage[h+1,0]=newimage[h,1]
    newimage[0,w+1]=newimage[1,w]
    newimage[h+1,w+1]=newimage[h,w]
    for i in range(1,h):
        newimage[i,0]=newimage[i,1]
        newimage[i,w+1]=newimage[i,w]
    for i in range(1,w+1):
        newimage[0,i]=newimage[1,i]
        newimage[h+1,i]=newimage[h,i]

    return newimage

def removepadding(img):
    h,w=img.shape
    newimage=np.zeros([h-2,w-2]).astype(np.uint8)
    for i in range(1,h-1):
        for j in range(1,w-1):
            newimage[i-1,j-1]=img[i,j]
    return newimage


def maxfilter(pimg):
    h,w=pimg.shape
    max_filter_image=np.zeros([h,w]).astype(np.uint8)
    for i in range(1,h-1):
        for j in range(1,w-1):
            maximum=0
            for l in range(i-1,i+2):
                for k in range(j-1,j+2):
                    if pimg[l,k]>maximum:
                            maximum=pimg[l,k]
            max_filter_image[i-1,j-1]=maximum 
    return max_filter_image   
             
def minfilter(pimg):
    h,w=pimg.shape
    min_filter_image=np.zeros([h,w]).astype(np.uint8)
    for i in range(1,h-1):
        for j in range(1,w-1):
            minimum=255
                      
            for l in range(i-1,i+2):
                for k in range(j-1,j+2):
                    if pimg[l,k]<minimum:
                        minimum=pimg[l,k]
            min_filter_image[i-1,j-1]=minimum   
    return min_filter_image          
                     
         
def meanfilter(pimg):
    h,w=pimg.shape
    mean_filter_image=np.zeros([h,w]).astype(np.uint8)
   
    for i in range(1,h-1):
        for j in range(1,w-1):
            sum=0
                      
            for l in range(i-1,i+2):
                for k in range(j-1,j+2):
                    sum+=pimg[l,k]
                    
            sum=np.round(sum/9)
            mean_filter_image[i-1,j-1]=sum
    return mean_filter_image
   
def medianfilter(pimg):
    h,w=pimg.shape
    median_filter_image=np.zeros([h,w]).astype(np.uint8)
    for i in range(1,h-1):
        for j in range(1,w-1):
            lst=[]            
            for l in range(i-1,i+2):
                for k in range(j-1,j+2):
                    key=pimg[l,k]
                    lst.append(key)
            lst.sort()   
            median_value=np.round(lst[4])
            median_filter_image[i-1,j-1]=median_value
    return median_filter_image               

im=cv2.imread('test.jpg',0)
newimage=samepadding(im)
removedimage=removepadding(newimage)
fig = plt.figure(figsize=(25, 25))
pltX = 1
pltY = 5
fig.add_subplot(pltX, pltY, 1)
plt.imshow(cv2.cvtColor(im,cv2.COLOR_BGR2RGB ))
plt.axis('off')
plt.title(" ORIGINAL IMAGE ")
max_filter_image=maxfilter(newimage)
fig.add_subplot(pltX, pltY, 2)
plt.imshow(cv2.cvtColor(max_filter_image, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.title(" MAXIMUM FILTER IMAGE ")
min_filter_image=minfilter(newimage)
fig.add_subplot(pltX, pltY, 3)
plt.imshow(cv2.cvtColor(min_filter_image,cv2.COLOR_BGR2RGB ))
plt.axis('off')
plt.title(" MINIMUM FILTER IMAGE ")
mean_filter_image=meanfilter(newimage)
fig.add_subplot(pltX, pltY, 4)
plt.imshow(cv2.cvtColor(mean_filter_image,cv2.COLOR_BGR2RGB ))
plt.axis('off')
plt.title(" MEAN FILTER IMAGE ")
median_filter_image=medianfilter(newimage)
fig.add_subplot(pltX, pltY, 5)
plt.imshow(cv2.cvtColor(median_filter_image,cv2.COLOR_BGR2RGB ))
plt.axis('off')
plt.title(" MEDIAN FILTER IMAGE ")
fig.show()
fig.waitforbuttonpress() 
    
