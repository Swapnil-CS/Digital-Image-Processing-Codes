import numpy as np
import matplotlib.pyplot as plt
import cv2

def main():
    img1=cv2.imread("img1.jpg",0)
    img2=cv2.imread("img2.jpg",0)
    img3=cv2.imread("test.jpg",0)
    img4=img3
    img1=cv2.resize(img1,(256,256))
    img2=cv2.resize(img2,(256,256))
    img3=cv2.resize(img3,(256,256))
    img4=cv2.resize(img4,(256,256))
    h,w=img1.shape
    x,y=img3.shape
    r1=np.zeros([h,w]).astype(np.uint8)
    r2=np.zeros([x,y]).astype(np.uint8)
    for i in range(h):
        for j in range(w):
            r1[i,j]=int(img1[i,j])-int(img2[i,j])
    for i in range(x):
        for j in range(y):
            r2[i,j]=img3[i,j]-img4[i,j]
    
    if np.sum(r1)==0:
        print("image 1 and 2 are same")
    else:
        print("image 1 and 2 are not same")
    
    if np.sum(r2)==0:
        print("image 3 and 4 are same")
    else:
        print("image 3 and 4 are not same")

    fig = plt.figure(figsize=(18, 18))
    pltX = 1
    pltY = 4

    fig.add_subplot(pltX, pltY, 1)
    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title(" IMAGE 1 ")
    fig.add_subplot(pltX, pltY, 2)
    plt.imshow(cv2.cvtColor(img2,cv2.COLOR_BGR2RGB ))
    plt.axis('off')
    plt.title(" IMAGE 2 ")

    fig.add_subplot(pltX, pltY, 3)
    plt.imshow(cv2.cvtColor(img3,cv2.COLOR_BGR2RGB ))
    plt.axis('off')
    plt.title(" IMAGE 3 ")
    
    fig.add_subplot(pltX, pltY, 4)
    plt.imshow(cv2.cvtColor(img3,cv2.COLOR_BGR2RGB ))
    plt.axis('off')
    plt.title(" IMAGE 4 ")
        

    fig.show()
    fig.waitforbuttonpress()

main()
