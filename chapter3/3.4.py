import cv2
import numpy as np

img1 = np.random.randint(0, 256, size=[3, 4], dtype=np.uint8)
img2 = np.random.randint(0, 256, size=[3, 4], dtype=np.uint8)
# img3= np.zeros((3,4), dtype=np.uint8)
gamma = 3
img3 = cv2.addWeighted(img1, 2, img2, 1, gamma)
print("img3=\n", img3)
