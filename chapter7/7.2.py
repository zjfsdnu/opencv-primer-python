import cv2

o = cv2.imread("../lenaNoise.png")
r5 = cv2.blur(o, (5, 5))
r30 = cv2.blur(o, (30, 30))
cv2.imshow("original", o)
cv2.imshow("result5", r5)
cv2.imshow("result30", r30)

cv2.waitKey(0)
cv2.destroyAllWindows()
