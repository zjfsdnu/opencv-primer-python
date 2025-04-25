import cv2

o = cv2.imread("../lena.bmp", cv2.IMREAD_GRAYSCALE)
r1 = cv2.Canny(o, 128, 200)
r2 = cv2.Canny(o, 32, 128)

cv2.imshow("original", o)
cv2.imshow("Canny 128-200", r1)
cv2.imshow("Canny 32-128", r2)

cv2.waitKey(0)
cv2.destroyAllWindows()
