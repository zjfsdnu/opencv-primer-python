import cv2

o = cv2.imread("../lenaNoise.png")
# r = cv2.bilateralFilter(o, -1, 100, 100)
r = cv2.bilateralFilter(o, 25, 100, 100)
cv2.imshow("original", o)
cv2.imshow("blurred", r)

cv2.waitKey(0)
cv2.destroyAllWindows()
