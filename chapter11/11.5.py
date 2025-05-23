import cv2

o = cv2.imread("../lena.bmp")
G0 = o
G1 = cv2.pyrDown(G0)
G2 = cv2.pyrDown(G1)
G3 = cv2.pyrDown(G2)
L0 = G0 - cv2.pyrUp(G1)
L1 = G1 - cv2.pyrUp(G2)
L2 = G2 - cv2.pyrUp(G3)
print("L0.shape=", L0.shape)
print("L1.shape=", L1.shape)
print("L2.shape=", L2.shape)

cv2.imshow("L0", L0)
cv2.imshow("L1", L1)
cv2.imshow("L2", L2)

cv2.waitKey(0)
cv2.destroyAllWindows()
