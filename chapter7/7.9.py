import cv2

o = cv2.imread("../bilTest.bmp")
g = cv2.GaussianBlur(o, (55, 55), 0)
b = cv2.bilateralFilter(o, 55, 100, 100)
cv2.imshow("original", o)
cv2.imshow("Gaussian", g)
cv2.imshow("bilateral", b)

cv2.waitKey(0)
cv2.destroyAllWindows()
