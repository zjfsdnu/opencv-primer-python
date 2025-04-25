import cv2

o = cv2.imread("../scharr.bmp", cv2.IMREAD_GRAYSCALE)
Scharry = cv2.Scharr(o, cv2.CV_64F, 0, 1)
Scharry = cv2.convertScaleAbs(Scharry)
cv2.imshow("Original", o)
cv2.imshow("Scharr", Scharry)

cv2.waitKey(0)
cv2.destroyAllWindows()
