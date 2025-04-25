import cv2

a = cv2.imread("../lenacolor.png", cv2.IMREAD_UNCHANGED)
face = a[220:400, 250:350]
cv2.imshow("original", a)
cv2.imshow("face", face)

cv2.waitKey(0)
cv2.destroyAllWindows()
