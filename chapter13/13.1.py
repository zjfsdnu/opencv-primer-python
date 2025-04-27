import cv2
import numpy as np
import matplotlib.pyplot as plt

o = cv2.imread('../boat.jpg')
cv2.imshow("original", o)

plt.hist(o.ravel(), 256)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
