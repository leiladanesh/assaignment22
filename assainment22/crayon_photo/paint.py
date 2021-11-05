
import cv2

img = cv2.imread("janan.png",0)

inverted = 255 - img
blurred = cv2.GaussianBlur(inverted,(21,21),0)
invert_blurred = 255 - blurred

sketch = img / invert_blurred
sketch = sketch * 255

cv2.imshow("crayon photo",sketch)
cv2.imwrite("janan.jpg ",sketch)
cv2.waitKey()

