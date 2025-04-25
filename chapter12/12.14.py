import cv2
import numpy as np

o = cv2.imread('../cc.bmp')
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)

rect = cv2.minAreaRect(contours[0])
print(rect)
box = cv2.boxPoints(rect)
print(box)
box = np.intp(box)
cv2.drawContours(o, [box], -1, (255, 255, 255), 2)

cv2.imshow('result', o)

cv2.waitKey(0)
cv2.destroyAllWindows()
