
import cv2

import numpy as np

import matplotlib.pyplot as plt

# function for mirroring an image


def imageRotationMirror(Bcha, Gcha, Rcha, img):

    row, col, chan = img.shape

    mirror_image = np.zeros((row, col, chan), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            mirror_image[i, col-j-1, 0] = Rcha[i, j]
            mirror_image[i, col-j-1, 1] = Gcha[i, j]
            mirror_image[i, col-j-1, 2] = Bcha[i, j]

    return mirror_image

# function for anti-clockwise rotation of an image


def imageRotationAnticlk(Bcha, Gcha, Rcha, img):

    row, col, chan = img.shape

    rotated_img_anticlk = np.zeros((col, row, chan), dtype=np.uint8)

    for i in range(col):
        for j in range(row):
            rotated_img_anticlk[col-i-1, j, 0] = Rcha[j, i]
            rotated_img_anticlk[col-i-1, j, 1] = Gcha[j, i]
            rotated_img_anticlk[col-i-1, j, 2] = Bcha[j, i]

    return rotated_img_anticlk

# function for clockwise rotation of an image


def imageRotationClk(Bcha, Gcha, Rcha, img):

    row, col, chan = img.shape

    rotated_img_clk = np.zeros((col, row, chan), dtype=np.uint8)

    for i in range(col):
        for j in range(row):
            rotated_img_clk[i, row-j-1, 0] = Rcha[j, i]
            rotated_img_clk[i, row-j-1, 1] = Gcha[j, i]
            rotated_img_clk[i, row-j-1, 2] = Bcha[j, i]

    return rotated_img_clk

# function for anti-clockwise rotation of an image and mirror it


def imageRotationAnticlkMirror(Bcha, Gcha, Rcha, img):

    row, col, chan = img.shape

    rotated_img_anticlk_mirror = np.zeros((col, row, chan), dtype=np.uint8)

    for i in range(col):
        for j in range(row):
            rotated_img_anticlk_mirror[i, j, 0] = Rcha[j, i]
            rotated_img_anticlk_mirror[i, j, 1] = Gcha[j, i]
            rotated_img_anticlk_mirror[i, j, 2] = Bcha[j, i]

    return rotated_img_anticlk_mirror

# function for clockwise rotation of an image and mirror it


def imageRotationClkMirror(Bcha, Gcha, Rcha, img):

    row, col, chan = img.shape

    rotated_img_clk_mirror = np.zeros((col, row, chan), dtype=np.uint8)

    for i in range(col):
        for j in range(row):
            rotated_img_clk_mirror[col-i-1, row-j-1, 0] = Rcha[j, i]
            rotated_img_clk_mirror[col-i-1, row-j-1, 1] = Gcha[j, i]
            rotated_img_clk_mirror[col-i-1, row-j-1, 2] = Bcha[j, i]

    return rotated_img_clk_mirror

# function for 180 degree rotation of an image


def imageUpsidedown(Bcha, Gcha, Rcha, img):

    row, col, chan = img.shape

    upsidedown_image = np.zeros((row, col, chan), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            upsidedown_image[row-i-1, col-j-1, 0] = Rcha[i, j]
            upsidedown_image[row-i-1, col-j-1, 1] = Gcha[i, j]
            upsidedown_image[row-i-1, col-j-1, 2] = Bcha[i, j]

    return upsidedown_image

# function of 180 degree rotation of an image and mirror it


def imageUpsidedownMirror(Bcha, Gcha, Rcha, img):

    row, col, chan = img.shape

    upsidedown_image_mirror = np.zeros((row, col, chan), dtype=np.uint8)

    for i in range(row):
        for j in range(col):
            upsidedown_image_mirror[row-i-1, j, 0] = Rcha[i, j]
            upsidedown_image_mirror[row-i-1, j, 1] = Gcha[i, j]
            upsidedown_image_mirror[row-i-1, j, 2] = Bcha[i, j]

    return upsidedown_image_mirror

# function for extracting the channels of original image


def channelExtraction(img):

    row, col, chan = img.shape

    Bcha = np.zeros((row, col), dtype=np.uint8)
    Gcha = np.zeros((row, col), dtype=np.uint8)
    Rcha = np.zeros((row, col), dtype=np.uint8)

    m = 0
    for i in img:
        n = 0
        for j in i:
            r, g, b = j
            Rcha[m, n] = r
            Gcha[m, n] = g
            Bcha[m, n] = b
            n += 1
        m += 1

    return Bcha, Gcha, Rcha


if __name__ == '__main__':

    img = cv2.imread(
        "F:/B.Sc 5th sem/Image Processing/Image Processing codes/6.jpg")

    # calling all the defined functions for different purposes
    Bcha, Gcha, Rcha = channelExtraction(img)

    mirror_image = imageRotationMirror(Bcha, Gcha, Rcha, img)

    rotated_img_anticlk = imageRotationAnticlk(Bcha, Gcha, Rcha, img)

    rotated_img_clk = imageRotationClk(Bcha, Gcha, Rcha, img)

    rotated_image_anticlk_mirror = imageRotationAnticlkMirror(
        Bcha, Gcha, Rcha, img)

    rotated_img_clk_mirror = imageRotationClkMirror(Bcha, Gcha, Rcha, img)

    upsidedown_image = imageUpsidedown(Bcha, Gcha, Rcha, img)

    upsidedown_image_mirror = imageUpsidedownMirror(Bcha, Gcha, Rcha, img)

    # using matplotlib to display all images in a single window
    fig = plt.figure(figsize=(50, 30))
    pltX = 2
    pltY = 4

    fig.add_subplot(pltX, pltY, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Original image")

    fig.add_subplot(pltX, pltY, 2)
    plt.imshow(cv2.cvtColor(rotated_img_anticlk, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Anti-Clockwise image")

    fig.add_subplot(pltX, pltY, 3)
    plt.imshow(cv2.cvtColor(rotated_img_clk, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Clockwise image")

    fig.add_subplot(pltX, pltY, 4)
    plt.imshow(cv2.cvtColor(upsidedown_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Upside down image")

    fig.add_subplot(pltX, pltY, 5)
    plt.imshow(cv2.cvtColor(mirror_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Mirror image")

    fig.add_subplot(pltX, pltY, 6)
    plt.imshow(cv2.cvtColor(rotated_image_anticlk_mirror, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Anti-Clockwise Mirror image")

    fig.add_subplot(pltX, pltY, 7)
    plt.imshow(cv2.cvtColor(rotated_img_clk_mirror, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Clockwise Mirror image")

    fig.add_subplot(pltX, pltY, 8)
    plt.imshow(cv2.cvtColor(upsidedown_image_mirror, cv2.COLOR_BGR2RGB))
    plt.axis('off')
    plt.title("Upside down Mirror image")

    fig.show()
    fig.waitforbuttonpress()

    ##cv2.imshow("Original image", img)
    ##cv2.imshow("Mirrored image", mirror_image)
    ##cv2.imshow("Rotated image anticlockwise", rotated_img_anticlk)
    ##cv2.imshow("Rotated image clockwise", rotated_img_clk)
    ##cv2.imshow("Rotated mirror image anticlockwise", rotated_image_anticlk_mirror)
    ##cv2.imshow("Rotated mirror image clockwise", rotated_img_clk_mirror)
    ##cv2.imshow("Up side down image", upsidedown_image)
    ##cv2.imshow("Up side down mirror image", upsidedown_image_mirror)

    # cv2.waitKey(0)
