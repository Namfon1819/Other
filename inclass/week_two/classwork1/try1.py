import cv2
import numpy as np

# Load the image
image = cv2.imread(r'C:\teacher\inclass\week_two\classwork1\12.jpg', 0)  


block_size = 30


for y in range(0, image.shape[0], block_size):
    for x in range(0, image.shape[1], block_size):
        # Get the current block
        block = image[y:y+block_size, x:x+block_size]

        transformed_block = cv2.equalizeHist(block)

        image[y:y+block_size, x:x+block_size] = transformed_block

cv2.imshow('Result', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
