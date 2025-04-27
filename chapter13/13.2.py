import cv2
import matplotlib.pyplot as plt

o = cv2.imread("../boat.bmp")
plt.hist(o.ravel(), 16)
plt.show()

# cv2.waitKey(0)
# cv2.destroyAllWindows()
