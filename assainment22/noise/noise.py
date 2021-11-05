
   
import random
import cv2
import numpy as np

img = cv2.imread("chess pieces.jpg" ,0)

row , col = img.shape

for i in range(10000):
    noise = random.randint(0,500)
    m = random.randint(0,row-1)
    n = random.randint(0,col-1)
    img[m,n] = noise 

cv2.imwrite('Add_noise.jpg',img)
cv2.imshow('noise',img)
cv2.waitKey()