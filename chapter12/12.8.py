import cv2

o1 = cv2.imread("../cs1.bmp")
gray = cv2.cvtColor(o1, cv2.COLOR_BGR2GRAY)
HuM1 = cv2.HuMoments(cv2.moments(gray)).flatten()
print("cv2.moments(gray)=\n", cv2.moments(gray))
print("\nHuM1=\n", HuM1)
print("\ncv2.moments(gray)['nu20']+cv2.moments(gray)['nu02']=%f+%f=%f\n"
      % (cv2.moments(gray)['nu20'], cv2.moments(gray)['nu02'],
         cv2.moments(gray)['nu20'] + cv2.moments(gray)['nu02']))
print("HuM1[0]=", HuM1[0])
print("\nHu[0]-(nu02+nu20)=",
      HuM1[0] - (cv2.moments(gray)['nu20'] + cv2.moments(gray)['nu02']))
