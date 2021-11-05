import cv2
import numpy as np

img1 = cv2.imread("leila.jpg",0)
img2 = cv2.imread("1.jpg",0)

img1 = cv2.resize(img1,(400,500))
img2 = cv2.resize(img2,(400,500))

pic1 = img1//2 + img2//8
pic2 = img1//2 + img2//4
pic3 = img1//2 + img2//2
pic4 = img1//4 + img2//2


result = np.concatenate((img1,pic1,pic2,pic4),axis=1)
cv2.imshow("Merge_pic",result)
cv2.imwrite("Merge_pic.jpg",result)
cv2.waitKey()

