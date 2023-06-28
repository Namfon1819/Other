import cv2 as cv
from matplotlib import pyplot as plt

#path_to_img = r"C:\teacher\image.jpg"
img = cv.imread(r"C:\teacher\assignment1\image.jpg")
img_h, img_w, _ = img.shape
split_width = 300
split_height = 300


def start_points(size, split_size, overlap=0):
    points = [0]
    stride = int(split_size * (1-overlap))
    counter = 1
    while True:
        pt = stride * counter
        if pt + split_size >= size:
            if split_size == size:
                break
            points.append(size - split_size)
            break
        else:
            points.append(pt)
        counter += 1
    return points


X_points = start_points(img_w, split_width, 0.5)
Y_points = start_points(img_h, split_height, 0.5)

count = 0
name = 'out1'
frmt = 'jpg'

for i in Y_points:
    for j in X_points:
        split = img[i:i+split_height, j:j+split_width]
        cv.imshow('Block', split)
        cv.waitKey(0)
        cv.imwrite('{}_{}.{}'.format(name, count, frmt), split)
        count += 1

cv.destroyAllWindows()
#img =cv.imread('split', 0)
#plt.hist(img.ravel(), 256, [0, 256])
#plt.show()
