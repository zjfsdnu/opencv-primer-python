import cv2
import numpy as np

img1 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
img2 = np.random.randint(0, 256, size=[3, 3], dtype=np.uint8)
print("img1=\n", img1)
print("img2=\n", img2)
img3 = cv2.add(img1, img2)
print("img3=\n", img3)
