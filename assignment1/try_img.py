import cv2 as cv

filename = r'C:\teacher\assignment1\image.jpg'
img = cv.imread(filename)

if img is not None:
    img_h, img_w, _ = img.shape
else:
    print("Failed")
