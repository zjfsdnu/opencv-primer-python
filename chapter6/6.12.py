import cv2

img = cv2.imread('../tiffany.bmp', 0)
t1, thd = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
t2, otsu = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
print("t1=", t1)
print("t2=", t2)
cv2.imshow("img", img)
cv2.imshow("thd=", thd)
cv2.imshow("otsu=", otsu)

cv2.waitKey(0)
cv2.destroyAllWindows()
