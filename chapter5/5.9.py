import cv2
import numpy as np

img = np.random.randint(0, 256, [4, 5], dtype=np.uint8)
mapx = np.ones(img.shape, np.float32) * 3
mapy = np.zeros(img.shape, np.float32)
rst = cv2.remap(img, mapx, mapy, cv2.INTER_LINEAR)
print("img=\n", img)
print("mapx=\n", mapx)
print("mapy=\n", mapy)
print("rst=\n", rst)
