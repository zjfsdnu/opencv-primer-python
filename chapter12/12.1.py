import cv2

o = cv2.imread("../contours.bmp")
cv2.imshow("o", o)
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_SIMPLE)
o = cv2.drawContours(o, contours, -1, (200, 200, 200), 10)
cv2.imshow("contours", o)

cv2.waitKey(0)
cv2.destroyAllWindows()
