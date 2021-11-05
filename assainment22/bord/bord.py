import cv2
import numpy as np

img1 = cv2.imread('board - origin.bmp', 0)
img2 = cv2.imread('board - test.bmp', 0)
img2 = img2[::,::-1]

result =cv2.absdiff(img1,img2)

cv2.imwrite('bord.jpg', result)
cv2.imshow('bord_difference',result)
cv2.waitKey()