import cv2
import numpy as np

img1 = cv2.imread("../blackhat.bmp")
img2 = cv2.imread("../lena.bmp")
k = np.ones((5, 5), np.uint8)
r1 = cv2.morphologyEx(img1, cv2.MORPH_BLACKHAT, k)
r2 = cv2.morphologyEx(img2, cv2.MORPH_BLACKHAT, k)
cv2.imshow("img1", img1)
cv2.imshow("result1", r1)
cv2.imshow("original", img2)
cv2.imshow("img2", r2)

cv2.waitKey(0)
cv2.destroyAllWindows()
