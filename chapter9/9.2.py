import cv2

o = cv2.imread("../sobel4.bmp", cv2.IMREAD_GRAYSCALE)
Soblex = cv2.Sobel(o, -1, 1, 0)
cv2.imshow("Original", o)
cv2.imshow("Sobel", Soblex)

cv2.waitKey(0)
cv2.destroyAllWindows()
