import cv2
import numpy as np

o = cv2.imread("../cs.bmp")
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
_, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

mask = np.zeros(gray.shape, np.uint8)
cnt = contours[0]
cv2.drawContours(mask, [cnt], -1, 255, -1)

leftmost = tuple(cnt[cnt[:, :, 0].argmin()][0])
rightmost = tuple(cnt[cnt[:, :, 0].argmax()][0])
topmost = tuple(cnt[cnt[:, :, 1].argmin()][0])
bottommost = tuple(cnt[cnt[:, :, 1].argmax()][0])

print(leftmost, rightmost, topmost, bottommost)

cv2.circle(o, leftmost, 2, (0, 0, 255), 2)
cv2.circle(o, rightmost, 2, (0, 0, 255), 2)
cv2.circle(o, topmost, 2, (0, 0, 255), 2)
cv2.circle(o, bottommost, 2, (0, 0, 255), 2)

leftmostLoc = (leftmost[0] - 15, leftmost[1] - 15)
rightmostLoc = rightmost
topmostLoc = topmost
bottommostLoc = (bottommost[0] + 10, bottommost[1] + 25)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(o, 'A', leftmostLoc, font, 1, (0, 0, 255), 2)
cv2.putText(o, 'B', rightmostLoc, font, 1, (0, 0, 255), 2)
cv2.putText(o, 'C', topmostLoc, font, 1, (0, 0, 255), 2)
cv2.putText(o, 'D', bottommostLoc, font, 1, (0, 0, 255), 2)

cv2.imshow("result", o)

cv2.waitKey(0)
cv2.destroyAllWindows()
