
import cv2 as cv

# Load the noisy image
img = cv.imread(r'C:\teacher\inclass\week_three\classwork\123.jpg', cv.IMREAD_GRAYSCALE)

# Convert the image to the appropriate type
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

# Apply Non-local Means Denoising
denoised_img = cv.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)

# Convert the image back to BGR if needed
denoised_img = cv.cvtColor(denoised_img, cv.COLOR_RGB2BGR)

# Display the denoised image
cv.imshow('Denoised Image', denoised_img)
cv.waitKey(0)
cv.destroyAllWindows()

