import cv2
import numpy as np

img = cv2.imread("../lena.bmp")
height, width = img.shape[:2]
x = 50
y = 100
M = np.float32([[1, 0, x], [0, 1, y]])
move = cv2.warpAffine(img, M, (width, height))
cv2.imshow("original", img)
cv2.imshow("move", move)

cv2.waitKey(0)
cv2.destroyAllWindows()
