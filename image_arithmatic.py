import cv2
import numpy as np
import matplotlib.pyplot as plt


def imageAddition(grayImg1,grayImg2):
    row,col = grayImg1.shape
    imgAdd = np.zeros((row,col), dtype=np.float32)
    for i in range(row):
        for j in range(col):
            imgAdd[i,j] = int(grayImg1[i,j]) +int( grayImg2[i,j])
    return imageNormalisation(imgAdd)    
  
def imageSubtraction(grayImg1,grayImg2):
    row,col = grayImg1.shape
    imgSub = np.zeros((row,col), dtype=np.float32)
    for i in range(row):
        for j in range(col):
            imgSub[i,j] = int(grayImg1[i,j]) - int( grayImg2[i,j])
    return imageNormalisation(imgSub)

def imageMultiplication(grayImg1,grayImg2):
    row,col = grayImg1.shape
    imgMul = np.zeros((row,col), dtype=np.float32)
    for i in range(row):
        for j in range(col):
            imgMul[i,j] = int(grayImg1[i,j]) * int(grayImg2[i,j])
    return imageNormalisation(imgMul)

def imageDivision(grayImg1,grayImg2):
    row,col = grayImg1.shape
    imgDiv = np.zeros((row,col), dtype=np.float32)
    for i in range(row):
        for j in range(col):
            if grayImg1[i,j]>0:
               imgDiv[i,j] = int (grayImg2[i,j]) // int(grayImg1[i,j])
            elif grayImg2[i,j]>0:
               imgDiv[i,j] = int (grayImg1[i,j]) // int(grayImg2[i,j])
            else:
                imgDiv[i,j] = int (grayImg1[i,j]) // int(grayImg2[i,j])
    return imageNormalisation(imgDiv)

def imageNormalisation(img):
    row,col = img.shape
    normalisedImg = np.zeros((row,col), dtype=np.uint8)
    min_pixel = np.min(img)
    max_pixel = np.max(img)
    for  i in range(row):
        for j in range(col):
            normalisedImg[i,j] = (255*(img[i,j] - min_pixel)/(max_pixel - min_pixel)).astype(int)             
    return normalisedImg


if __name__ == '__main__':
    img1 = cv2.imread("img1.jpg", 0)
    img2 = cv2.imread("img2.jpg", 0)

    imgAdd = imageAddition(img1, img2)
    imgSub = imageSubtraction(img1, img2)
    imgMul = imageMultiplication(img1, img2)
    imgDiv = imageDivision(img1, img2)

    fig = plt.figure(figsize=(30, 18))
    pltX = 3
    pltY = 2

    fig.add_subplot(pltX, pltY, 1)
    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Gray image 1")

    fig.add_subplot(pltX, pltY, 2)
    plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Gray image 2")

    fig.add_subplot(pltX, pltY, 3)
    plt.imshow(cv2.cvtColor(imgAdd, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Image Addition")

    fig.add_subplot(pltX, pltY, 4)
    plt.imshow(cv2.cvtColor(imgSub, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Image Subtraction")

    fig.add_subplot(pltX, pltY, 5)
    plt.imshow(cv2.cvtColor(imgMul, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Image Multiplication")

    fig.add_subplot(pltX, pltY, 6)
    plt.imshow(cv2.cvtColor(imgDiv, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Image Division")

    fig.show()
    fig.waitforbuttonpress()
