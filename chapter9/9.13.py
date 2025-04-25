import cv2

o = cv2.imread("../lena.bmp", cv2.IMREAD_GRAYSCALE)

Soblex = cv2.Sobel(o, cv2.CV_64F, 1, 0, ksize=3)
Sobley = cv2.Sobel(o, cv2.CV_64F, 0, 1, ksize=3)
Soblex = cv2.convertScaleAbs(Soblex)
Sobley = cv2.convertScaleAbs(Sobley)
Sobelxy = cv2.addWeighted(Soblex, 0.5, Sobley, 0.5, 0)

Scharrx = cv2.Scharr(o, cv2.CV_64F, 1, 0)
Scharry = cv2.Scharr(o, cv2.CV_64F, 0, 1)
Scharrx = cv2.convertScaleAbs(Scharrx)
Scharry = cv2.convertScaleAbs(Scharry)
Scharrxy = cv2.addWeighted(Scharrx, 0.5, Scharry, 0.5, 0)

cv2.imshow("Original", o)
cv2.imshow("Sobel", Sobelxy)
cv2.imshow("Scharr", Scharrxy)

cv2.waitKey(0)
cv2.destroyAllWindows()
