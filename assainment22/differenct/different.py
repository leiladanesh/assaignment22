import cv2
import numpy as np

img1= cv2.imread('a.tif', 0)
img2 = cv2.imread('b.tif', 0)

result = img2 - img1

cv2.imwrite('different.jpg', result)
cv2.imshow('different', result)
cv2.waitKey()