import cv2
import numpy as np

img = cv2.imread('D:/Swapnil &arnab/6.jpg')
row,col,chan = img.shape
print(row,col,chan)
##print(img)
R=np.zeros((row,col),dtype=np.int8)
G=np.zeros((row,col),dtype=np.int8)
B=np.zeros((row,col),dtype=np.int8)
print(img.shape)
##print(type(img))
m = 0
for i in img:
    n = 0
    for j in i:
        r,g,b = j
        R[m,n] = r
        G[m,n] = g
        B[m,n] = b
        n = n+1    
    m = m+1
    
##cv2.imshow("r-img",R)
##cv2.imshow("g-img",G)
##cv2.imshow("b-img",B)
##        print(r,g,b)
cv2.imshow('display',(R+G+B)/3)
cv2. waitKey(0)

