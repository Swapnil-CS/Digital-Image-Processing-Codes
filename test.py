import cv2
from cv2 import imread
from cv2 import waitKey

import numpy as np

img = cv2.imread(
    'F:\B.Sc 5th sem\Image Processing\Image Processing codes\house-simple-cartoon-icon-vector-24871943.jpg')
print(img)

cv2.imshow('Display', img)
waitKey(0)
