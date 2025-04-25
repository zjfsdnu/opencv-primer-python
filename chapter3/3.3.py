import cv2

a = cv2.imread("../lena.bmp")
b = a
result1 = a + b
result2 = cv2.add(a, b)
cv2.imshow("result1", result1)
cv2.imshow("result2", result2)

cv2.waitKey(0)
cv2.destroyAllWindows()
