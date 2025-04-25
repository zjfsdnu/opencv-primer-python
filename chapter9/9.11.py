import cv2

o = cv2.imread("../scharr.bmp", cv2.IMREAD_GRAYSCALE)
Scharrxy11 = cv2.Scharr(o, cv2.CV_64F, 1, 1)
cv2.imshow("Original", o)
cv2.imshow("Scharr", Scharrxy11)

cv2.waitKey(0)
cv2.destroyAllWindows()
