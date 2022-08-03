import numpy as np
import cv2

img1=cv2.imread("Lenna_SaltPepper1.bmp",cv2.IMREAD_GRAYSCALE)
img2 = img1.copy()
nr,nc=img1.shape[:2]
g=np.zeros((3,3),dtype="float")
for r in range(1,nr,1):
    for c in range(1,nc,1):
        if  img1[r,c] == 0 or img1[r,c]==255 :
            for x in range(3):
                for y in range(3):
                    g[x,y]=img1[r+x-2,c+y-2]
                    for x1 in range(3):
                        for y1 in range(3):
                            if g[x1,y1]>g[x,y]:
                                g[x1,y1],g[x,y]=g[x,y],g[x1,y1]
            img2[r,c]=g[1,1]  
cv2.imshow( "Original Image",img1 )
cv2.imshow( "composite laplacian", img2)	
cv2.waitKey(0)
cv2.destroyAllWindows()
