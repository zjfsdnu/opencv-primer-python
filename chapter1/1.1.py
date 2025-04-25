import cv2

lena = cv2.imread('../lenacolor.png')
# print(lena)
# cv2.namedWindow("lesson")
cv2.imshow('lesson', lena)
cv2.waitKey(0)