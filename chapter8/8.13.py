import cv2

o = cv2.imread("../kernel.bmp", cv2.IMREAD_UNCHANGED)
kernel1 = cv2.getStructuringElement(cv2.MORPH_RECT, (59, 59))
kernel2 = cv2.getStructuringElement(cv2.MORPH_CROSS, (59, 59))
kernel3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (59, 59))
dst1 = cv2.dilate(o, kernel1, iterations=1)
dst2 = cv2.dilate(o, kernel2, iterations=1)
dst3 = cv2.dilate(o, kernel3, iterations=1)
cv2.imshow("original", o)
cv2.imshow("dst1", dst1)
cv2.imshow("dst2", dst2)
cv2.imshow("dst3", dst3)

cv2.waitKey(0)
cv2.destroyAllWindows()
