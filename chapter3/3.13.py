import cv2
import numpy as np

lena = cv2.imread("../lena.bmp", 0)
cv2.imshow("lena", lena)
r, c = lena.shape
x = np.zeros((r, c, 8), dtype=np.uint8)
for i in range(8):
    x[:, :, i] = 2 ** i

ri = np.zeros((r, c, 8), dtype=np.uint8)
for i in range(8):
    ri[:, :, i] = cv2.bitwise_and(lena, x[:, :, i])
    mask = ri[:, :, i] > 0
    ri[mask] = 255
    cv2.imshow(str(i), ri[:, :, i])

cv2.waitKey(0)
cv2.destroyAllWindows()
