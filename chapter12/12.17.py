import cv2
import numpy as np

o = cv2.imread('../cc.bmp')
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)

rows, cols = gray.shape
[vx, vy, x, y] = cv2.fitLine(contours[0], cv2.DIST_L2, 0, 0.01, 0.01)
lefty = int(-x * vy / vx + y)
righty = int(((cols - x) * vy / vx) + y)
cv2.line(o, (cols - 1, righty), (0, lefty), (0, 255, 0), 2)

cv2.imshow('result', o)

cv2.waitKey(0)
cv2.destroyAllWindows()
