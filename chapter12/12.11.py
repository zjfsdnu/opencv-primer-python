import cv2

o = cv2.imread('../cc.bmp')
gray = cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(binary, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)

x, y, w, h = cv2.boundingRect(contours[0])
print("顶点及长宽的点形式:")
print(x, y, w, h)

rect = cv2.boundingRect(contours[0])
print("\n顶点及长宽的元组（tuple）形式：")
print(rect)
