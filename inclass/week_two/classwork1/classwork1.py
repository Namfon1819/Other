import cv2
import numpy as np

# Load the image
image = cv2.imread(r'C:\teacher\inclass\week_two\classwork1\12.jpg')  # Read the image

# Define the block size and color
block_size = 16  # Adjust this value according to your needs
block_color = (0, 255, 0)  # Set the color of the blocks (in BGR format)

# Iterate over each block
for y in range(0, image.shape[0], block_size):
    for x in range(0, image.shape[1], block_size):
        # Get the current block
        block = image[y:y+block_size, x:x+block_size]

        # Apply intensity transformation or histogram equalization on the block
        transformed_block = cv2.equalizeHist(block)

        # Draw a rectangle around the block with the specified color
        cv2.rectangle(image, (x, y), (x+block_size, y+block_size), block_color, thickness=2)

        # Replace the original block with the transformed block
        image[y:y+block_size, x:x+block_size] = transformed_block

# Display the result
cv2.imshow('Result', image)
cv2.waitKey(0)
cv2.destroyAllWindows()