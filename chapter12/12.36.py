import cv2
import numpy as np

o = cv2.imread("../cc.bmp")
cv2.imshow("original", o)
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]

mask1 = np.zeros(gray.shape, np.uint8)
cv2.drawContours(mask1, [cnt], -1, 255, 2)
pixelpoints1 = cv2.findNonZero(mask1)
print(pixelpoints1.shape)
print(pixelpoints1)
cv2.imshow("mask1", mask1)

mask2 = np.zeros(gray.shape, np.uint8)
cv2.drawContours(mask2, [cnt], -1, 255, -1)
pixelpoints2 = cv2.findNonZero(mask2)
print(pixelpoints2.shape)
print(pixelpoints2)
cv2.imshow("mask2", mask2)

cv2.waitKey(0)
cv2.destroyAllWindows()
