import cv2

lena = cv2.imread('../lenacolor.png')
cv2.imshow("demo", lena)
key = cv2.waitKey(0)
if key != -1:
    print("key pressed", key)
