import cv2

img = cv2.imread('../lena.bmp', 0)
cv2.imshow("before", img)
for i in range(10, 100):
    for j in range(80, 100):
        img[i, j] = 255
cv2.imshow("after", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
