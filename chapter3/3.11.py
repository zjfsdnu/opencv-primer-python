import cv2
import numpy as np

a = cv2.imread("../lenacolor.png", 1)
h, w = a.shape[:2]
m = np.zeros((h, w), dtype=np.uint8)
m[100:400, 200:400] = 255
m[100:500, 100:200] = 255
c = cv2.bitwise_and(a, a, mask=m)
print("a.shape=", a.shape)
print("mask.shape=", m.shape)
cv2.imshow("a", a)
cv2.imshow("mask", m)
cv2.imshow("c", c)

cv2.waitKey(0)
cv2.destroyAllWindows()
