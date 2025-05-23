import cv2

o = cv2.imread("../lena.bmp")
up = cv2.pyrUp(o)
down = cv2.pyrDown(up)
diff = down - o
print("o.shape=", o.shape)
print("down.shape=", down.shape)

cv2.imshow("original", o)
cv2.imshow("down", down)
cv2.imshow("diff", diff)

cv2.waitKey(0)
cv2.destroyAllWindows()
