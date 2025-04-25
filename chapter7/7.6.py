import cv2

o = cv2.imread("../lenaNoise.png")
r1 = cv2.GaussianBlur(o, (5, 5), 0, 0)
r2 = cv2.GaussianBlur(o, (5, 5), 0.1, 0.1)
r3 = cv2.GaussianBlur(o, (5, 5), 1, 1)
cv2.imshow("original", o)
cv2.imshow("result1", r1)
cv2.imshow("result2", r2)
cv2.imshow("result3", r3)

cv2.waitKey(0)
cv2.destroyAllWindows()
