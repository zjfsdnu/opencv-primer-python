import cv2

o = cv2.imread("../sobel4.bmp", cv2.IMREAD_GRAYSCALE)
Soblexy = cv2.Sobel(o, cv2.CV_64F, 1, 1)
Soblexy = cv2.convertScaleAbs(Soblexy)
cv2.imshow("Original", o)
cv2.imshow("Sobel", Soblexy)

cv2.waitKey(0)
cv2.destroyAllWindows()
