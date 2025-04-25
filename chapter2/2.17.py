import cv2

lena = cv2.imread("../lenacolor.png")
b, g, r = cv2.split(lena)
cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)

cv2.waitKey(0)
cv2.destroyAllWindows()
