import cv2
import numpy as np

img = cv2.imread("../erode.bmp", cv2.IMREAD_UNCHANGED)
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=1)
cv2.imshow("original", img)
cv2.imshow("erosion", erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()

