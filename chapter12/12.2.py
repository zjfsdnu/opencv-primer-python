import cv2
import numpy as np

o = cv2.imread('../contours.bmp')
cv2.imshow('Original', o)
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)

n = len(contours)
contoursImg = []
for i in range(n):
    contoursImg.append(np.zeros(o.shape, np.uint8))
    cv2.drawContours(contoursImg[i], contours, i, (255, 255, 255), 5)
    cv2.imshow('contours' + str(i), contoursImg[i])

for i in range(n):
    contoursImg.append(np.zeros(o.shape, np.uint8))
    cv2.drawContours(contoursImg[i + n], contours, i, (255, 255, 255), -1)
    cv2.imshow('contours' + str(i + n), contoursImg[i + n])

cv2.waitKey(0)
cv2.destroyAllWindows()
