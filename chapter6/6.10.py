import cv2
import numpy as np

img = cv2.imread("../lena.bmp")
t, rst = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
cv2.imshow("img", img)
cv2.imshow("rst", rst)

cv2.waitKey(0)
cv2.destroyAllWindows()
