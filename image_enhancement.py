import numpy as np
import matplotlib.pyplot as plt
import cv2 

def main():
    img=cv2.imread("test.jpg",0)
    fig = plt.figure(figsize=(30, 30))
    pltX = 2
    pltY = 3
    fig.add_subplot(pltX, pltY, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("ORIGINAL")
    
    negative_image=negim(img)
    fig.add_subplot(pltX, pltY, 2)
    plt.imshow(cv2.cvtColor(negative_image,cv2.COLOR_BGR2RGB ))
    plt.axis('off')
    plt.title("NEGATIVE")
    
    log_image=logimg(img)
    fig.add_subplot(pltX, pltY, 3)
    plt.imshow(cv2.cvtColor(log_image,cv2.COLOR_BGR2RGB ))
    plt.axis('off')
    plt.title("LOG TRANSFORMATION")

    powerlaw_transformed_image= powerlaw(img)
    fig.add_subplot(pltX, pltY, 4)
    plt.imshow(cv2.cvtColor(powerlaw_transformed_image,cv2.COLOR_BGR2RGB ))
    plt.axis('off')
    plt.title(" POWERLAW TRANSFORMATION")

    piecewise_linear_transformed_image=Piecewise_linear_transform(img)
    fig.add_subplot(pltX, pltY, 5)
    plt.imshow(cv2.cvtColor(piecewise_linear_transformed_image,cv2.COLOR_BGR2RGB ))
    plt.axis('off')
    plt.title("PIECEWISE LINEAR TRANSFORMATION")
    fig.show()
    fig.waitforbuttonpress()

    


def negim(im):
    h,w=im.shape
    newIm=np.zeros([h,w]).astype(np.uint8)
   
    for i in range(h):
        for j in range(w):
            newIm[i][j]=255-im[i][j]
    return(newIm)

def logimg(img):
    row, col = img.shape
    logImg = np.zeros((row, col), dtype=np.uint8)
    max_pixel_val = np.max(img)
    C = 255/(np.log(1 + max_pixel_val))
    for i in range(row):
        for j in range(col):
            logImg[i, j] = round(C * np.log(1 + img[i, j]))
    return logImg

def powerlaw(img):
    row, col = img.shape
    gammaImg = np.zeros((row, col), dtype=np.uint8)
    max_pixel_val = np.max(img)
    y=2.1
    C = 255/(np.log(255**3 + max_pixel_val))
    C = 0.005
    for i in range(row):
        for j in range(col):
            gammaImg[i, j] = round(C * (img[i, j]**y))
    return gammaImg


def Piecewise_linear_transform(im):
    a=int(input("enter the number for a "))
    b=int(input("enter the number for b "))
    m,n=255,0
    h,w=im.shape
    for i in range(h):
        for j in range(w):
         if im[i][j]<m:
            m=im[i][j]
         if im[i][j]>n:
            n=im[i][j]
    new=im
    h,w=new.shape
    r=(b-a)/(n-m)
    for i in range(h):
        for j in range(w):
            new[i][j]=a+r*(im[i][j])
    return new
        

    


main()
