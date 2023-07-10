import cv2 as cv
import random

img = cv.imread(r'C:\teacher\inclass\week_three\classwork\234.jpg', cv.IMREAD_GRAYSCALE)

original_img = img.copy()
density_salt = 0.1
density_pepper = 0.1

number_of_white_pixel = int(density_salt * (img.shape[0] * img.shape[1]))

for i in range(number_of_white_pixel):
    y_coord = random.randint(0, img.shape[0] - 1)
    x_coord = random.randint(0, img.shape[1] - 1)
    img[y_coord][x_coord] = 255
    
number_of_block_pixel = int(density_pepper * (img.shape[0] * img.shape[1]))

for i in range(number_of_block_pixel):
    y_coord = random.randint(0, img.shape[0] - 1)
    x_coord = random.randint(0, img.shape[1] - 1)
    img[y_coord][x_coord] = 0
    
    
cv.imwrite('output.png', img)   
cv.imwrite('original.png', original_img)


noisy_img = cv.imread('output.png', cv.IMREAD_GRAYSCALE)
denoisy_img = cv.medianBlur(noisy_img, 5)
cv.imwrite('denoisy.png',denoisy_img)



