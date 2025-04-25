import cv2

o = cv2.imread('../cc.bmp')
cv2.imshow('original', o)

gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)

adp = o.copy()
epsilon = 0.1 * cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
adp = cv2.drawContours(adp, [approx], -1, (0, 0, 255), 2)
cv2.imshow('result0.1', adp)

adp = o.copy()
epsilon = 0.09 * cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
adp = cv2.drawContours(adp, [approx], -1, (0, 0, 255), 2)
cv2.imshow('result0.09', adp)

adp = o.copy()
epsilon = 0.055 * cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
adp = cv2.drawContours(adp, [approx], -1, (0, 0, 255), 2)
cv2.imshow('result0.055', adp)

adp = o.copy()
epsilon = 0.05 * cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
adp = cv2.drawContours(adp, [approx], -1, (0, 0, 255), 2)
cv2.imshow('result0.05', adp)

adp = o.copy()
epsilon = 0.02 * cv2.arcLength(contours[0], True)
approx = cv2.approxPolyDP(contours[0], epsilon, True)
adp = cv2.drawContours(adp, [approx], -1, (0, 0, 255), 2)
cv2.imshow('result0.02', adp)

cv2.waitKey(0)
cv2.destroyAllWindows()
