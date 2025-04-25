import cv2
import numpy as np

img = np.random.randint(-356, 356, size=[4, 5], dtype=np.int16)
rst = cv2.convertScaleAbs(img)
print("img:\n", img)
print("rst:\n", rst)
