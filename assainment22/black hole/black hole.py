import cv2
import numpy as np

images =[]
for i in range(1,6):
    img = cv2.imread(f"1/{i}.jpg",0)
    images.append(img)
    row , col = img.shape
result1 = np.zeros((row,col),dtype="uint8")

for image in images:
    result1 += image//5
images.clear()

for i in range(1,6):
    img = cv2.imread(f"2/{i}.jpg",0)
    images.append(img)
result2 = np.zeros((row,col),dtype="uint8")

for image in images:
    result2 += image//5
images.clear()

for i in range(1,6):
    img = cv2.imread(f"3/{i}.jpg",0)
    images.append(img)
result3 = np.zeros((row,col),dtype= "uint8")

for image in images:
    result3 += image//5
images.clear()

for i in range(1,6):
    img = cv2.imread(f"4/{i}.jpg",0)
    images.append(img)
result4 = np.zeros((row,col),dtype="uint8")
for image in images:
    result4 += image//5

pic1 = np.concatenate((result1,result2),axis=1)
pic2 = np.concatenate((result3,result4),axis=1)
resualt = np.concatenate((pic1,pic2),axis=0)
resualt = cv2.resize(resualt,(500,500))
cv2.imshow("Galaxy",resualt)
cv2.imwrite("Galaxy.jpg",resualt)
cv2.waitKey()