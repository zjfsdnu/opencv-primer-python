import cv2

lena = cv2.imread("../lenacolor.png")
cv2.imshow("lena1", lena)

b = lena[:, :, 0]
g = lena[:, :, 1]
r = lena[:, :, 2]
cv2.imshow("b", b)
cv2.imshow("g", g)
cv2.imshow("r", r)

lena[:, :, 0] = 0
cv2.imshow("lenab0", lena)
lena[:, :, 1] = 0
cv2.imshow("lenab0g0", lena)

cv2.waitKey(0)
cv2.destroyAllWindows()
