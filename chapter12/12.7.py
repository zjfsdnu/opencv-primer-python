import cv2
import numpy as np

o = cv2.imread('../contours0.bmp')
cv2.imshow('original', o)

gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)

n = len(contours)
cntLen = []
for i in range(n):
    cntLen.append(cv2.arcLength(contours[i], True))
    print('contours' + str(i) + ':', cntLen[i])

cntLenSum = sum(cntLen)
cntLenAvg = cntLenSum / n
print('contours总长度:', cntLenSum)
print('contours平均长度:', cntLenAvg)

contoursImg = []
for i in range(n):
    contoursImg.append(np.zeros(o.shape, np.uint8))
    cv2.drawContours(contoursImg[i], contours, i, (255, 255, 255), 3)
    if cntLen[i] > cntLenAvg:
        cv2.imshow('contours' + str(i), contoursImg[i])
        print('contours' + str(i) + '的长度大于平均长度')

cv2.waitKey(0)
cv2.destroyAllWindows()
