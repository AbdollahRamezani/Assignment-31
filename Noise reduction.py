import numpy as np
import cv2

image = cv2.imread("input/xray_noisy.png", cv2.IMREAD_GRAYSCALE)
rows, cols = image.shape
result = np.zeros((rows, cols), dtype=np.uint8)

# filter = np.array([[1/9, 1/9, 1/9],
#                   [1/9, 1/9, 1/9],
#                   [1/9, 1/9, 1/9]])

filter = np.ones((3, 3)) / 9

for i in range(1, rows-1):
    for j in range(1, cols-1):
        small = image[i-1:i+2, j-1:j+2]  
        average = np.sum(filter * small)  
        result[i, j] = average

cv2.imwrite("output/noise reduction_xray_noisy.png", result)        