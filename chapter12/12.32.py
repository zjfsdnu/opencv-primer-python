import cv2
import numpy as np

o = cv2.imread("../cc.bmp")
cv2.imshow("original", o)
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
retval = cv2.fitEllipse(contours[0])
print(retval)
(x, y), (MA, ma), angle = cv2.fitEllipse(contours[0])
print(x)
print(y)
print(MA)
print(ma)
print(angle)

cv2.ellipse(o, retval, (0, 255, 0), 2)
cv2.imshow("result", o)

cv2.waitKey(0)
cv2.destroyAllWindows()
