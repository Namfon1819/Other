import numpy as np
import cv2 as cv

img = cv.imread(r'C:\teacher\inclass\week_two\out2.jpg', cv.IMREAD_GRAYSCALE)

output = cv.medianBlur(img, 20)

cv.imwrite('Median [1] input.png', img)
cv.imwrite('Median [2] output.png', output)