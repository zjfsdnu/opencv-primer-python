import cv2

o = cv2.imread("../scharr.bmp", cv2.IMREAD_GRAYSCALE)
Scharrx = cv2.Scharr(o, cv2.CV_64F, 1, 0)
Scharrx = cv2.convertScaleAbs(Scharrx)
cv2.imshow("Original", o)
cv2.imshow("Scharr", Scharrx)

cv2.waitKey(0)
cv2.destroyAllWindows()
