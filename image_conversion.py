import cv2

import numpy as np

import matplotlib.pyplot as plt

# function for extracting the channels of original image


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

# function for converting a color image to corresponding gray image using specified formula


def grayConversion(B, G, R):

    row, col = B.shape
    gray_chan = np.zeros((row, col), dtype=np.uint8)

    for i in range(row):

        for j in range(col):
            gray_chan[i, j] = round(R[i, j]*0.3 + G[i, j]*0.59 + B[i, j]*0.11)

    return gray_chan

# function for converting a color image to corresponding gray image using average


def grayConversionAvg(B, G, R):

    row, col = B.shape
    gray_chan_avg = np.zeros((row, col), dtype=np.uint8)

    for i in range(row):

        for j in range(col):
            gray_chan_avg[i, j] = round((R[i, j] + G[i, j] + B[i, j])/3)

    return gray_chan_avg

# function for converting a gray image to corresponding negative image


def grayToNegative(grayImg):

    row, col = grayImg.shape
    negativeChan = np.zeros((row, col), dtype=np.uint8)

    for i in range(row):

        for j in range(col):
            negativeChan[i, j] = abs(grayImg[i, j] - 255)

    return negativeChan

# function to convert an color image to corresponding negative image


def colorToNegative(B, G, R, img):

    row, col, chan = img.shape

    negative_of_color = np.zeros((row, col, chan), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            negative_of_color[i, j, 0] = 255 - R[i, j]
            negative_of_color[i, j, 1] = 255 - G[i, j]
            negative_of_color[i, j, 2] = 255 - B[i, j]

    return negative_of_color

# function to convert an rgb image to ycbcr image


def RGB_To_yCbCr(B, G, R, img):

    row, col, chan = img.shape

    yCbCr_image = np.zeros((row, col, chan), dtype=np.uint8)

    for i in range(row):
        for j in range(col):

            yCbCr_image[i, j, 0] = round(
                R[i, j]*0.299 + G[i, j]*0.587 + B[i, j]*0.114)
            # yCbCr_image[i, j, 0] = (y * 219)+16
            yCbCr_image[i, j, 1] = round(
                R[i, j]*0.500 - G[i, j]*0.418688 - B[i, j]*0.081312)
            # yCbCr_image[i, j, 1] = (Cr * 224) + 128
            yCbCr_image[i, j, 2] = round(-R[i, j] *
                                         0.168736 - G[i, j]*0.331264 + B[i, j]*0.500)
            # yCbCr_image[i, j, 2] = (Cb * 224) + 128

    return yCbCr_image


if __name__ == '__main__':

    img = cv2.imread(
        "F:/B.Sc 5th sem/Image Processing/Image Processing codes/6.jpg")

    # calling the defined functions for different purposes
    B, G, R = channelExtraction(img)

    grayImg = grayConversion(B, G, R)

    grayImg_avg = grayConversionAvg(B, G, R)

    negative_of_gray = grayToNegative(grayImg)

    negative_of_color = colorToNegative(B, G, R, img)

    yCbCr_image = RGB_To_yCbCr(B, G, R, img)

    # using matplotlib to display all the images in an single window
    fig = plt.figure(figsize=(30, 18))
    pltX = 2
    pltY = 3

    fig.add_subplot(pltX, pltY, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Original Image")

    fig.add_subplot(pltX, pltY, 2)
    plt.imshow(cv2.cvtColor(grayImg, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Gray image using formula")

    fig.add_subplot(pltX, pltY, 3)
    plt.imshow(cv2.cvtColor(grayImg_avg, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Gray image using average")

    fig.add_subplot(pltX, pltY, 4)
    plt.imshow(cv2.cvtColor(negative_of_gray, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Negative of Gray image")

    fig.add_subplot(pltX, pltY, 5)
    plt.imshow(cv2.cvtColor(negative_of_color, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Negative of Color image")

    fig.add_subplot(pltX, pltY, 6)
    plt.imshow(cv2.cvtColor(yCbCr_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("yCbCr image of RGB image")

    fig.show()
    fig.waitforbuttonpress()

    # cv2.imshow('Original Image', img)
    # cv2.imshow('Gray Image display by formula', grayImg)
    # cv2.imshow('Gray Image display by Average', grayImg_avg)
    # cv2.imshow('Negative image of Gray image', negative_of_gray)
    # cv2.imshow('Negative image of color image', negative_of_color)
    # cv2.imshow('YCbCr from RGB image', yCbCr_image)
    # cv2. waitKey(0)
