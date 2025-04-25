import cv2

o = cv2.imread("../sobel4.bmp", cv2.IMREAD_GRAYSCALE)
Soblex = cv2.Sobel(o, cv2.CV_64F, 1, 0)
Sobley = cv2.Sobel(o, cv2.CV_64F, 0, 1)
Soblex = cv2.convertScaleAbs(Soblex)
Sobley = cv2.convertScaleAbs(Sobley)
Sobelxy = cv2.addWeighted(Soblex, 0.5, Sobley, 0.5, 0)
cv2.imshow("Original", o)
cv2.imshow("Sobel", Sobelxy)

cv2.waitKey(0)
cv2.destroyAllWindows()
