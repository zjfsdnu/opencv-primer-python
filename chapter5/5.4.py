import cv2

img = cv2.imread("../lena.bmp")
x = cv2.flip(img, 0)
y = cv2.flip(img, 1)
xy = cv2.flip(img, -1)
cv2.imshow("img", img)
cv2.imshow("x", x)
cv2.imshow("y", y)
cv2.imshow("xy", xy)

cv2.waitKey(0)
cv2.destroyAllWindows()
