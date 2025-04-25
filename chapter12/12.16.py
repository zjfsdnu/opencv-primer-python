import cv2
import numpy as np

o = cv2.imread('../cc.bmp')
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)

ellipse = cv2.fitEllipse(contours[0])
print(ellipse)
cv2.ellipse(o, ellipse, (0, 255, 255), 3)

cv2.imshow('result', o)

cv2.waitKey(0)
cv2.destroyAllWindows()
