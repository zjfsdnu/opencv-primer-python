import cv2

img = cv2.imread("../lena.bmp", 0)
print("读取像素点 img.item(3,2)=", img.item(3, 2))
img.itemset((3, 2), 255)
print("修改后读取像素点 img.item(3,2)=", img.item(3, 2))
cv2.imshow("before", img)

for i in range(10,100):
    for j in range(80,100):
        img.itemset((i, j), 255)

cv2.imshow("after", img)

cv2.waitKey(0)
cv2.destroyAllWindows()
