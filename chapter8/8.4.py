import numpy as np
import cv2

img = np.zeros((5, 5), np.uint8)
img[2:3, 1:4] = 1
kernel = np.ones((3, 1), np.uint8)
dilation = cv2.dilate(img, kernel, iterations=1)
print("img=\n", img)
print("kernel=\n", kernel)
print("dilation=\n", dilation)
