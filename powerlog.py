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


def gammaCorrection(grayImg, y):

    row, col = grayImg.shape

    gammaImg = np.zeros((row, col), dtype=np.uint8)

    max_pixel_val = np.max(grayImg)

    C = 255/(np.log(255**3 + max_pixel_val))
    C = 0.005

    for i in range(row):

        for j in range(col):

            gammaImg[i, j] = round(C * (grayImg[i, j]**y))

    return gammaImg


if __name__ == "__main__":

    img = cv2.imread("D:/Swapnil &arnab/6.jpg")

    B, G, R = channelExtraction(img)

    grayImg = grayConversion(B, G, R)

    gamma_1 = gammaCorrection(grayImg, 1.8)

    gamma_2 = gammaCorrection(grayImg, 2.1)

    gamma_3 = gammaCorrection(grayImg, 2.5)

    fig = plt.figure(figsize=(30, 18))
    pltX = 2
    pltY = 2

    fig.add_subplot(pltX, pltY, 1)
    plt.imshow(grayImg, cmap="gray")
    plt.axis('off')
    plt.title("Gray image")

    fig.add_subplot(pltX, pltY, 2)
    plt.imshow(cv2.cvtColor(gamma_1, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Gamma 1.8")

    fig.add_subplot(pltX, pltY, 3)
    plt.imshow(cv2.cvtColor(gamma_2, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Gamma 2.1")

    fig.add_subplot(pltX, pltY, 4)
    plt.imshow(cv2.cvtColor(gamma_3, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Gamma 2.5")

    fig.show()
