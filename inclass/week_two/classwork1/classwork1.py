import cv2
import numpy as np


image = cv2.imread(r'C:\teacher\inclass\week_two\123.jpg', cv2.IMREAD_GRAYSCALE) 

start = (0, 200) #p1
end = (400, 200) #p2
line = (500, 500, 500)  #สีขาวหรือสีอะไรก็ได้แล้วแต่เรากำหนด

output_image = np.zeros_like(image) # ทุกอย่างนอกจากเส้นคือ 0

cv2.line(output_image, start, end, line, thickness=2)

cv2.imshow("Output Image", output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


