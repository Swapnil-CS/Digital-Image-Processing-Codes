import cv2

import numpy as np

import matplotlib.pyplot as plt


def channelExtraction(img):

    row, col, chan = img.shape
    Rchan = np.zeros((row, col), dtype=np.uint8)
    Gchan = np.zeros((row, col), dtype=np.uint8)
    Bchan = np.zeros((row, col), dtype=np.uint8)

    m = 0
    for i in img:
        n = 0
        for j in i:
            r, g, b = j
            Rchan[m, n] = r
            Gchan[m, n] = g
            Bchan[m, n] = b
            n = n+1
        m = m+1

    return Bchan, Gchan, Rchan


def grayConversion(B, G, R):

    row, col = B.shape
    gray_chan = np.zeros((row, col), dtype=np.uint8)

    for i in range(row):

        for j in range(col):
            gray_chan[i, j] = R[i, j]*0.3 + G[i, j]*0.59 + B[i, j]*0.11

    return gray_chan


def logTransformation(grayImg):

    row, col = grayImg.shape

    logImg = np.zeros((row, col), dtype=np.uint8)

    max_pixel_val = np.max(grayImg)

    C = 255/(np.log(1 + max_pixel_val))

    for i in range(row):

        for j in range(col):

            logImg[i, j] = round(C * np.log(1 + grayImg[i, j]))

    return logImg


def colorLogTransformation(B, G, R):

    row, col = B.shape

    color_logImg = np.zeros((row, col, 3), dtype=np.uint8)

    Bmax_pixel_val = np.max(B)

    B_C = 255/(np.log(1 + Bmax_pixel_val))

    Gmax_pixel_val = np.max(G)

    G_C = 255/(np.log(1 + Gmax_pixel_val))

    Rmax_pixel_val = np.max(R)

    R_C = 255/(np.log(1 + Rmax_pixel_val))

    for i in range(row):

        for j in range(col):

            color_logImg[i, j, 0] = round(R_C * np.log(1 + R[i, j]))
            color_logImg[i, j, 1] = round(G_C * np.log(1 + G[i, j]))
            color_logImg[i, j, 2] = round(B_C * np.log(1 + B[i, j]))

    return color_logImg


if __name__ == "__main__":

    img = cv2.imread(
        "F:/B.Sc 5th sem/Image Processing/Image Processing codes/6.jpg")

    B, G, R = channelExtraction(img)

    grayImg = grayConversion(B, G, R)

    logImg = logTransformation(grayImg)

    color_logImg = colorLogTransformation(B, G, R)

    fig = plt.figure(figsize=(30, 18))
    pltX = 2
    pltY = 2

    fig.add_subplot(pltX, pltY, 1)
    plt.imshow(cv2.cvtColor(grayImg, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Gray image")

    fig.add_subplot(pltX, pltY, 2)
    plt.imshow(cv2.cvtColor(logImg, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Log Transformed Gray image")

    fig.add_subplot(pltX, pltY, 3)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Original Color image")

    fig.add_subplot(pltX, pltY, 4)
    plt.imshow(cv2.cvtColor(color_logImg, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Log Transformed Color image")

    fig.show()
    fig.waitforbuttonpress()
