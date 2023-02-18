import numpy as np
import cv2 
import matplotlib.pyplot as plt


def filter(kx, ky, img):
    m = int(np.floor(len(kx) / 2))
    n = int(np.floor(len(list(zip(*kx)))) / 2)
    rows, cols = img.shape                                                            # no of rows and cols
    filtered_img = np.zeros((rows, cols), np.uint8)                                    # new integer image is created
    for i in range(m, rows - m):
        for j in range(n, cols - n):
            sumx = sumy = 0
            for x in range(-m, m + 1, 1):
                for y in range(-n, n + 1, 1):
                    sumx = sumx + (img[i + x, j + y] * kx[m + x][n + y])            # sum of product of kernal elements with corresponding image elements
                    sumy = sumy + (img[i + x, j + y] * ky[m + x][n + y])
            filtered_img[i, j] = abs(sumx) + abs(sumy)
    return filtered_img

img = cv2.imread("test.jpg",0)
y = [[0, 0, 0], [0, -1, 0], [0, 0, 1]]
x = [[0, 0, 0], [0, 0, -1], [0, 1, 0]]
robert = filter(x, y, img)
y = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
x = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
sobel = filter(x, y, img)
y = [[-1, -1, -1], [0, 0, 0], [1, 1, 1]]
x = [[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]]
prewitt = filter(x, y, img)

fig = plt.figure(figsize=(18, 18))
pltX = 1
pltY = 4
fig.add_subplot(pltX, pltY, 1)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB ))
plt.axis('off')
plt.title("ORIGINAL IMAGE")

fig.add_subplot(pltX, pltY, 2)
plt.imshow(cv2.cvtColor(robert,cv2.COLOR_BGR2RGB ))
plt.axis('off')
plt.title("USING ROBERT OPERATOR")
fig.add_subplot(pltX, pltY, 3)
plt.imshow(cv2.cvtColor(sobel,cv2.COLOR_BGR2RGB ))
plt.axis('off')
plt.title("USING SOBEL OPERATOR")
fig.add_subplot(pltX, pltY, 4)
plt.imshow(cv2.cvtColor(prewitt,cv2.COLOR_BGR2RGB ))
plt.axis('off')
plt.title("USING PREWITT OPERATOR")
fig.show()
fig.waitforbuttonpress()
    
