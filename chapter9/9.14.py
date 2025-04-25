import cv2

o = cv2.imread("../laplacian.bmp", cv2.IMREAD_GRAYSCALE)
laplacian = cv2.Laplacian(o, cv2.CV_64F)
laplacian = cv2.convertScaleAbs(laplacian)

cv2.imshow("Original", o)
cv2.imshow("Laplacian", laplacian)

cv2.waitKey(0)
cv2.destroyAllWindows()
