import cv2
import numpy as np

img1 = np.ones((4, 4), dtype=np.uint8) * 3
img2 = np.ones((4, 4), dtype=np.uint8) * 5
img3 = np.ones((4, 4), dtype=np.uint8) * 66
m = np.zeros((4, 4), dtype=np.uint8)
m[2:4, 2:4] = 1
print("img1=\n", img1)
print("img2=\n", img2)
print("mask=\n", m)
print("初始值 img3=\n", img3)
img3 = cv2.add(img1, img2, mask=m)
print("求和后 img3=\n", img3)
