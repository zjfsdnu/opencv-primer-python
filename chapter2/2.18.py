import cv2

lena = cv2.imread("../lenacolor.png")
b, g, r = cv2.split(lena)
rgb = cv2.merge([r, g, b])
bgr = cv2.merge([b, g, r])
cv2.imshow("Original", lena)
cv2.imshow("RGB", rgb)
cv2.imshow("BGR", bgr)

cv2.waitKey(0)
cv2.destroyAllWindows()
