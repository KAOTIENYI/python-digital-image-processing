
import cv2
img1=cv2.imread("Lena.jpg",-1)
nr,nc=img1.shape[:2]
scale=eval(input("please enter scale:"))
nr2=int(nr*scale)
nc2=int(nc*scale)
img2=cv2.resize(img1,(nr2,nc2),interpolation=cv2.INTER_LINEAR)
cv2.imshow("1",img1)
cv2.imshow("2",img2)
cv2.waitKey(0)
