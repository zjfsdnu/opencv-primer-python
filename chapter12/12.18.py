import cv2

o = cv2.imread('../cc.bmp')
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)

area, trg1 = cv2.minEnclosingTriangle(contours[0])
print(area, trg1)
for i in range(0, 3):
    # cv2.line(o, tuple(trg1[i][0]), tuple(trg1[(i + 1) % 3][0]), (0, 255, 0), 2)
    print(tuple(trg1[i][0]))
    cv2.line(o, (int(trg1[i][0][0]), int(trg1[i][0][1])),
             (int(trg1[(i + 1) % 3][0][0]), int(trg1[(i + 1) % 3][0][1])),
             (0, 255, 0), 2)

cv2.imshow('result', o)

cv2.waitKey(0)
cv2.destroyAllWindows()
