import cv2
import numpy as np

a = cv2.imread("../lenacolor.png", cv2.IMREAD_UNCHANGED)
cv2.imshow("original", a)
face = np.random.randint(0, 256, size=[180, 100, 3], dtype=np.uint8)
a[220:400, 250:350] = face
cv2.imshow("result", a)

cv2.waitKey(0)
cv2.destroyAllWindows()
