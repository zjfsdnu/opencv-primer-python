import cv2

o = cv2.imread("../lena.bmp", cv2.IMREAD_GRAYSCALE)

r1 = cv2.pyrDown(o)
r2 = cv2.pyrDown(r1)
r3 = cv2.pyrDown(r2)

print("o.shape=", o.shape)
print("r1.shape=", r1.shape)
print("r2.shape=", r2.shape)
print("r3.shape=", r3.shape)

cv2.imshow("o", o)
cv2.imshow("r1", r1)
cv2.imshow("r2", r2)
cv2.imshow("r3", r3)

cv2.waitKey(0)
cv2.destroyAllWindows()
