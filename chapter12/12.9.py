import cv2

o1 = cv2.imread("../cs1.bmp")
gray1 = cv2.cvtColor(o1, cv2.COLOR_BGR2GRAY)
HuM1 = cv2.HuMoments(cv2.moments(gray1)).flatten()
o2 = cv2.imread("../cs3.bmp")
gray2 = cv2.cvtColor(o2, cv2.COLOR_BGR2GRAY)
HuM2 = cv2.HuMoments(cv2.moments(gray2)).flatten()
o3 = cv2.imread("../lena512.bmp")
gray3 = cv2.cvtColor(o3, cv2.COLOR_BGR2GRAY)
HuM3 = cv2.HuMoments(cv2.moments(gray3)).flatten()

print("o1.shape=", o1.shape)
print("o2.shape=", o2.shape)
print("o3.shape=", o3.shape)

print("cv2.moments(gray1)=\n", cv2.moments(gray1))
print("cv2.moments(gray2)=\n", cv2.moments(gray2))
print("cv2.moments(gray3)=\n", cv2.moments(gray3))

print("HuM1=\n", HuM1)
print("HuM2=\n", HuM2)
print("HuM3=\n", HuM3)

print("HuM1-HuM2=\n", HuM1 - HuM2)
print("HuM1-HuM3=\n", HuM1 - HuM3)

cv2.imshow("original1", o1)
cv2.imshow("original2", o2)
cv2.imshow("original3", o3)

cv2.waitKey(0)
cv2.destroyAllWindows()
