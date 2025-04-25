import cv2
import numpy as np

a = np.zeros((5, 5), dtype=np.uint8)
for times in range(10):
    i = np.random.randint(0, 5)
    j = np.random.randint(0, 5)
    a[i, j] = 1

print("a=\n", a)
loc = cv2.findNonZero(a)
print(loc)
