import cv2

o = cv2.imread('../contours.bmp')
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)

hull = cv2.convexHull(contours[0])
print(hull)
hull2 = cv2.convexHull(contours[0], returnPoints=False)
print(hull2)
