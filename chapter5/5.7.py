import cv2
import numpy as np

img = cv2.imread("../lena.bmp")
rows, cols = img.shape[:2]
p1 = np.float32([[0, 0], [cols - 1, 0], [0, rows - 1]])
p2 = np.float32([[0, rows * 0.33], [cols * 0.85, rows * 0.25], [cols * 0.15, rows * 0.7]])
M = cv2.getAffineTransform(p1, p2)
dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow("original", img)
cv2.imshow("affine", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
