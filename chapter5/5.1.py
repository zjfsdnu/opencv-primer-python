import numpy as np
import cv2

img = np.ones([2, 4, 3], dtype=np.uint8)
size = img.shape[:2]
rst = cv2.resize(img, size)
print("img.shape:", img.shape)
print("img:\n", img)
print("rst.shape:", rst.shape)
print("rst:\n", rst)
