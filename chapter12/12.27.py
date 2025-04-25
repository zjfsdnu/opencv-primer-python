import cv2

o1 = cv2.imread("../cs.bmp")
o2 = cv2.imread("../cs3.bmp")
o3 = cv2.imread("../hand.bmp")
cv2.imshow("original1", o1)
cv2.imshow("original2", o2)
cv2.imshow("original3", o3)

gray1 = cv2.cvtColor(o1, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(o2, cv2.COLOR_BGR2GRAY)
gray3 = cv2.cvtColor(o3, cv2.COLOR_BGR2GRAY)

_, binary1 = cv2.threshold(gray1, 127, 255, cv2.THRESH_BINARY)
_, binary2 = cv2.threshold(gray2, 127, 255, cv2.THRESH_BINARY)
_, binary3 = cv2.threshold(gray3, 127, 255, cv2.THRESH_BINARY)

contours1, _ = cv2.findContours(binary1, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours2, _ = cv2.findContours(binary2, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours3, _ = cv2.findContours(binary3, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

cnt1 = contours1[0]
cnt2 = contours2[0]
cnt3 = contours3[0]

hd = cv2.createHausdorffDistanceExtractor()

d1 = hd.computeDistance(cnt1, cnt1)
print(d1)
d2 = hd.computeDistance(cnt1, cnt2)
print(d2)
d3 = hd.computeDistance(cnt1, cnt3)
print(d3)

cv2.waitKey(0)
cv2.destroyAllWindows()
