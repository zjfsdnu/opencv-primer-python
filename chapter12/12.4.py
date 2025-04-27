import cv2
import numpy as np

o = cv2.imread("../moments.bmp")
cv2.imshow("original", o)
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)

n = len(contours)
contoursImg = []
for i in range(n):
    contoursImg.append(np.zeros(o.shape, np.uint8))
    cv2.drawContours(contoursImg[i], contours, i, (255, 255, 255), 3)
    cv2.imshow("contours" + str(i), contoursImg[i])

print("观察各个轮廓的矩（moments）:")
for i in range(n):
    M = cv2.moments(contours[i])
    print("contours" + str(i) + ":", M)

print("观察各个轮廓的面积（area）:")
for i in range(n):
    area = cv2.moments(contours[i])['m00']
    print("contours" + str(i) + ":", area)

cv2.waitKey(0)
cv2.destroyAllWindows()
