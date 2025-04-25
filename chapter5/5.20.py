import numpy as np
import cv2

img = cv2.imread('../lena.bmp')
rows, cols = img.shape[:2]
mapx = np.zeros((rows, cols), np.float32)
mapy = np.zeros((rows, cols), np.float32)
for i in range(rows):
    for j in range(cols):
        if 0.25 * rows <= i < 0.75 * rows and 0.25 * cols <= j < 0.75 * cols:
            mapx.itemset((i, j), 2 * (j - cols * 0.25) + 0.5)
            mapy.itemset((i, j), 2 * (i - rows * 0.25) + 0.5)
        else:
            mapx.itemset((i, j), 0)
            mapy.itemset((i, j), 0)

rst = cv2.remap(img, mapx, mapy, interpolation=cv2.INTER_LINEAR)
cv2.imshow('original', img)
cv2.imshow('result', rst)

cv2.waitKey(0)
cv2.destroyAllWindows()
