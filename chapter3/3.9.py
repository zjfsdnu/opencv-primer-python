import cv2
import numpy as np

a = cv2.imread("../lenacolor.png", 1)
b = np.zeros(a.shape, dtype=np.uint8)
b[100:400, 200:400] = 255
b[100:500, 100:200] = 255
c = cv2.bitwise_and(a, b)
print("a.shape=", a.shape)
print("b.shape=", b.shape)
cv2.imshow("a", a)
cv2.imshow("b", b)
cv2.imshow("c", c)

cv2.waitKey(0)
cv2.destroyAllWindows()
