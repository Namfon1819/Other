import numpy as np
import cv2 as cv 

#Read the image
img = cv.imread("out.png")

print("Data type of image (OpenCV): ",type(img))

# Display the image
cv.imshow("Example1-imshow", img)

#Save the image
cv.imwrite("2.png", img)

#Wait for a key press 
cv.waitKey(0)

#Clean up  
cv.destroyAllWindows()