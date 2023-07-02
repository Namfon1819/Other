import cv2
import matplotlib.pyplot as plt

img = cv2.imread(r"C:\teacher\assignment1\image.jpg")
if img is None:
    print("Error: Failed to read the image file.")
else:
    plt.hist(img.ravel(), 256, [0, 256])
    plt.show()
