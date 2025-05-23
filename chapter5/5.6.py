import cv2

img = cv2.imread("../lena.bmp")
height, width = img.shape[:2]
M = cv2.getRotationMatrix2D((width / 2, height / 2), 45, 0.6)
rotate = cv2.warpAffine(img, M, (width, height))
cv2.imshow("original", img)
cv2.imshow("rotate", rotate)

cv2.waitKey(0)
cv2.destroyAllWindows()
