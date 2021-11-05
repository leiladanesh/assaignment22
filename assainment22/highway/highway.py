import cv2
import numpy as np
images = []
for i in range(0,15):
    img = cv2.imread(f"highway/h{i}.jpg",0)
    images.append(img)
    row , col = img.shape

result = np.zeros((row,col),dtype="uint8")
for img in images:
    result += img//15

result = cv2.resize(result,(500,500))
cv2.imshow("HighWay",result)
cv2.imwrite('HighWay.jpg',result)
cv2.waitKey()



