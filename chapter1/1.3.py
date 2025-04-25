import cv2

lena = cv2.imread('../lenacolor.png')
cv2.imshow("demo", lena)
key = cv2.waitKey(0)
if key == ord('a'):
    cv2.imshow("PressA", lena)
elif key == ord('b'):
    cv2.imshow("PressB", lena)
cv2.waitKey(0)
