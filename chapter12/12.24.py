import cv2

o =cv2.imread('../cs.bmp')
cv2.imshow('original', o)
gray=cv2.cvtColor(o, cv2.COLOR_BGR2GRAY)
ret,binary=cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
contours,_=cv2.findContours(binary,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

hull=cv2.convexHull(contours[0])
cv2.polylines(o,[hull], True, (0,255,0),2)

distA=cv2.pointPolygonTest(hull, (300,150), True)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(o, "A", (300,150), font , 1,(0,255,0), 3)
print('distA=', distA)

distB=cv2.pointPolygonTest(hull, (300,250), True)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(o, "B", (300,250), font , 1,(0,255,0), 3)
print('distB=', distB)

distC=cv2.pointPolygonTest(hull, (423,112), True)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(o, "C", (423,112), font , 1,(0,255,0), 3)
print('distC=', distC)

cv2.imshow("result", o)

cv2.waitKey(0)
cv2.destroyAllWindows()