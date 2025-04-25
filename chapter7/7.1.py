import cv2

o = cv2.imread("../lenaNoise.png")
r = cv2.blur(o, (5, 5))
cv2.imshow("original", o)
cv2.imshow("blurred", r)

cv2.waitKey(0)
cv2.destroyAllWindows()
