import numpy as np
import cv2

lena = cv2.imread("../lena512.bmp", 0)
watermark = cv2.imread("../watermark.bmp", 0)
w = watermark[:, :] > 0
watermark[w] = 1

r, c = lena.shape
t254 = np.ones((r, c), dtype=np.uint8) * 254
lenaH7 = cv2.bitwise_and(lena, t254)
e = cv2.bitwise_or(lenaH7, watermark)

t1 = np.ones((r, c), dtype=np.uint8)
wm = cv2.bitwise_and(e, t1)
print(wm)

w = wm[:, :] > 0
watermark[w] = 255

cv2.imshow("lena", lena)
cv2.imshow("watermark", watermark)
cv2.imshow("watermarked", e)
cv2.imshow("watermark recovered", watermark)

cv2.waitKey(0)
cv2.destroyAllWindows()
