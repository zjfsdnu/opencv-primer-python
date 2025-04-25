import cv2

o = cv2.imread('../hand.bmp')
cv2.imshow('original', o)
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, mode=cv2.RETR_TREE, method=cv2.CHAIN_APPROX_SIMPLE)

cnt=contours[0]
hull = cv2.convexHull(cnt, returnPoints=False)
defects = cv2.convexityDefects(cnt, hull)
print(defects)

for i in range(defects.shape[0]):
    s, e, f, d = defects[i, 0]
    start = tuple(cnt[s][0])
    end = tuple(cnt[e][0])
    far = tuple(cnt[f][0])
    cv2.line(o, start, end, (0, 0,255), 2)
    cv2.circle(o, far, 5, (255, 0, 0), -1)

cv2.imshow('result', o)

cv2.waitKey(0)
cv2.destroyAllWindows()
