import cv2

o = cv2.imread("../lenaNoise.png")
r = cv2.boxFilter(o, -1, (5, 5), normalize=False)
cv2.imshow("original", o)
cv2.imshow("result5", r)
print(r)

cv2.waitKey(0)
cv2.destroyAllWindows()
