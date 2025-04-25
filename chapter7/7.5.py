import cv2

o = cv2.imread("../lenaNoise.png")
r1 = cv2.boxFilter(o, cv2.CV_16U, (5, 5), normalize=False)
r2 = cv2.boxFilter(o, cv2.CV_16U, (16, 16), normalize=False)
r3 = r1 * 10
cv2.imshow("original", o)
cv2.imshow("result1", r1)
cv2.imshow("result2", r2)
cv2.imshow("result3", r3)

cv2.waitKey(0)
cv2.destroyAllWindows()
