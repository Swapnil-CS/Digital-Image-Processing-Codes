import cv2

import numpy as np


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


def grayConversionAvg(B, G, R):

    row, col = B.shape
    gray_chan_avg = np.zeros((row, col), dtype=np.uint8)

    for i in range(row):

        for j in range(col):
            gray_chan_avg[i, j] = (R[i, j] + G[i, j] + B[i, j])//3

    return gray_chan_avg


def grayToNegative(grayImg):

    row, col = grayImg.shape
    negativeChan = np.zeros((row, col), dtype=np.uint8)

    for i in range(row):

        for j in range(col):
            negativeChan[i, j] = abs(grayImg[i, j] - 255)

    return negativeChan


def colorToNegative(B, G, R, img):

    row, col, chan = img.shape

    negative_of_color = np.zeros((row, col, chan), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            negative_of_color[i, j, 0] = 255 - R[i, j]
            negative_of_color[i, j, 1] = 255 - G[i, j]
            negative_of_color[i, j, 2] = 255 - B[i, j]

    return negative_of_color


img = cv2.imread(
    "F:/B.Sc 5th sem/Image Processing/Image Processing codes/6.jpg")

B, G, R = channelExtraction(img)

grayImg = grayConversion(B, G, R)

grayImg_avg = grayConversionAvg(B, G, R)

negative_of_gray = grayToNegative(grayImg)

negative_of_color = colorToNegative(B, G, R, img)

cv2.imshow('Original Image', img)
cv2.imshow('Gray Image display by formula', grayImg)
cv2.imshow('Gray Image display by Average', grayImg_avg)
cv2.imshow('Negative image of Gray image', negative_of_gray)
cv2.imshow('Negative image of color image', negative_of_color)
cv2. waitKey(0)
