import cv2

o =cv2.imread('../hand.bmp')
cv2.imshow('original', o)
gray=cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret,binary=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours,_=cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

image1=o.copy()
hull=cv2.convexHull(contours[0])
cv2.polylines(image1, [hull],True, (0, 255, 0), 2)
print(cv2.isContourConvex(hull))
cv2.imshow('result1', image1)

image2=o.copy()
epsilon=0.01*cv2.arcLength(contours[0], True)
approx=cv2.approxPolyDP(contours[0], epsilon, True)
cv2.drawContours(image2, [approx], -1, (0, 0, 255), 2)
print(cv2.isContourConvex(approx))
cv2.imshow('result2', image2)

cv2.waitKey(0)
cv2.destroyAllWindows()