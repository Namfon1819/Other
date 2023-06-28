import numpy as np 
import cv2 as cv

img = cv.imread(r'C:\teacher\inclass\out1.jpg', cv.IMREAD_GRAYSCALE)

filterSize = 15;
kernel = np.ones((filterSize,filterSize), np.float32)/(filterSize*2)

output = cv.filter2D(img, -1, kernel, borderType = cv.BORDER_REFLECT)

cv.imwrite("Average [1] input.png", img)
cv.imwrite("Average [2] output.png", output)