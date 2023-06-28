import numpy as np
import cv2 as cv

img = cv.imread(r'C:\teacher\inclass\week_two\out2.jpg', cv.IMREAD_GRAYSCALE)
ksize = (31,31);
sigmaX = 5.0;
output = cv.GaussianBlur(img, ksize, sigmaX, borderType= cv.BORDER_REFLECT)

cv.imwrite("Gaussian [1] input.png", img)
cv.imwrite("Gaussian [2] output.png", output)