import cv2

o1 = cv2.imread("../cs1.bmp")
o2 = cv2.imread("../cs2.bmp")
o3 = cv2.imread("../cc.bmp")
gray1 = cv2.cvtColor(o1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(o2, cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(o3, cv2.COLOR_BGR2GRAY)
_, binary1 = cv2.threshold(gray1, 127, 255, cv2.THRESH_BINARY)
_, binary2 = cv2.threshold(gray2, 127, 255, cv2.THRESH_BINARY)
_, binary3 = cv2.threshold(gray3, 127, 255, cv2.THRESH_BINARY)
contours1, _ = cv2.findContours(binary1, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)
contours2, _ = cv2.findContours(binary2, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)
contours3, _ = cv2.findContours(binary3, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)

cnt1 = contours1[0]
cnt2 = contours2[0]
cnt3 = contours3[0]
# ret0 = cv2.matchShapes(cnt1, cnt1, 1, 0)
# ret1 = cv2.matchShapes(cnt1, cnt2, 1, 0)
# ret2 = cv2.matchShapes(cnt1, cnt3, 1, 0)
ret0 = cv2.matchShapes(gray1, gray1, 1, 0)
ret1 = cv2.matchShapes(gray1, gray2, 1, 0)
ret2 = cv2.matchShapes(gray1, gray3, 1, 0)
print("o1.shape=", o1.shape)
print("o2.shape=", o2.shape)
print("o3.shape=", o3.shape)
print("相同图像的匹配值=", ret0)
print("相似图像的匹配值=", ret1)
print("不相似图像的匹配值=", ret2)

cv2.imshow("o1", o1)
cv2.imshow("o2", o2)
cv2.imshow("o3", o3)

cv2.waitKey(0)
cv2.destroyAllWindows()
