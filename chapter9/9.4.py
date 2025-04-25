import cv2

o = cv2.imread("../sobel4.bmp", cv2.IMREAD_GRAYSCALE)
Sobley = cv2.Sobel(o, cv2.CV_64F, 0, 1)
Sobley = cv2.convertScaleAbs(Sobley)
cv2.imshow("Original", o)
cv2.imshow("Sobel", Sobley)

cv2.waitKey(0)
cv2.destroyAllWindows()
