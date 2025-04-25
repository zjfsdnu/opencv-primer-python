import cv2

a = cv2.imread("../boat.bmp")
b = cv2.imread("../lena512.bmp")
result = cv2.addWeighted(a, 0.6, b, 0.4, 0)
cv2.imshow("boat", a)
cv2.imshow("lena", b)
cv2.imshow("result", result)

cv2.waitKey(0)
cv2.destroyAllWindows()
