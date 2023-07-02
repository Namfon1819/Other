import numpy as np
import cv2 as cv

img = cv.imread(r"C:\teacher\assignment1\image.jpg")
img_h, img_w, _ = img.shape
image = np.random.randn(4, 4, 3)
tiles = np.zeros((4, 2, 2, 3))

c = 0

for i in range(0, image.shape[1], 2):  

    for j in range(0, image.shape[2], 2):

        tiles[c] = image[i:i+2, j:j+2, :]
        cv.imshow('Block',tiles)
        c += 1
cv.destroyAllWindows()