import numpy as np
import matplotlib.pyplot as plt
import cv2

def avg(img1,img2):
    h,w=img1.shape
    result=np.zeros([h,w]).astype(np.uint16)
    for i in range(h):
        for j in range(w):
            result[i,j]=(int(img1[i,j])+int(img2[i,j]))//2
    return result

if __name__ == '__main__':
    img1=cv2.imread('img1.jpg',0)
    img2=cv2.imread('img2.jpg',0)

    result = avg(img1,img2)

    fig = plt.figure(figsize=(30, 18))
    pltX = 1
    pltY = 3

    fig.add_subplot(pltX, pltY, 1)
    plt.imshow(cv2.cvtColor(img1, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("IMAGE 1")

    fig.add_subplot(pltX, pltY, 2)
    plt.imshow(cv2.cvtColor(img2, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("IMAGE 2")

    fig.add_subplot(pltX, pltY, 3)
    plt.imshow(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("AVERAGE IMAGE")
                                 
    fig.show()
    fig.waitforbuttonpress()




