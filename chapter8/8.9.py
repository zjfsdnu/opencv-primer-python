import cv2
import numpy as np

o = cv2.imread("../gradient.bmp")
# o = cv2.imread("../lenacolor.png")
k = np.ones((5, 5), np.uint8)
r = cv2.morphologyEx(o, cv2.MORPH_GRADIENT, k, iterations=1)
cv2.imshow("img1", o)
cv2.imshow("result1", r)

cv2.waitKey(0)
cv2.destroyAllWindows()
