import numpy as np
import cv2

image = cv2.imread("input/building.png", cv2.IMREAD_GRAYSCALE)
rows, cols = image.shape
result_1 = np.zeros((rows, cols), dtype=np.uint8)
result_2 = np.zeros((rows, cols), dtype=np.uint8)

filter_horizontal = np.array([[-1, -1, -1],
                              [0, 0, 0],
                              [1, 1, 1]])

filter_vertical = np.array([[2, 0, -2],
                              [2, 0, -2],
                              [2, 0, -2]])

for i in range(1, rows-1):
    for j in range(1, cols-1):
        small_1 = image[i-1:i+2, j-1:j+2]  
        average_1 = np.abs(np.sum(filter_horizontal * small_1))
        result_1[i, j] = average_1

for i in range(1, rows-1):
    for j in range(1, cols-1):
        small_2 = image[i-1:i+2, j-1:j+2]  
        average_2= np.abs(np.sum(filter_vertical * small_2))
        result_2[i, j] = average_2     

result = np.add(result_1, result_2)
cv2.imwrite("output/vertical_horizontal edge detection_building.png", result)        