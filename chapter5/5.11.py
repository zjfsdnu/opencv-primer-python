import cv2
import numpy as np

img = cv2.imread('../lena.bmp')
height, width = img.shape[:2]
mapx = np.zeros(img.shape[:2], np.float32)
mapy = np.zeros(img.shape[:2], np.float32)
for i in range(height):
    for j in range(width):
        mapx.itemset((i, j), j)
        mapy.itemset((i, j), i)

rst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)
cv2.imshow('original', img)
cv2.imshow('rst', rst)

cv2.waitKey(0)
cv2.destroyAllWindows()
