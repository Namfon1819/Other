import numpy as np
import cv2 as cv

img = np.zeros([300, 300], dtype=np.uint8)

center_1 = (135, 100)
radius_1 = 30

center_2 = (180, 100)
radius_2 = 30

cv.circle(img, center_1, radius_1, 200, -1)
cv.circle(img, center_2, radius_2, 200, -1)

cv.imshow('Drawing', img)
cv.waitKey(0)
cv.destroyAllWindows()

#หนูงงกับโจทย์ได้มาแบบนี้ค่าาา