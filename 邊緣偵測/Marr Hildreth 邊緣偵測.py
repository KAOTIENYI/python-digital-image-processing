import numpy as np
import cv2


def Marr_Hildreth(f):
    T=2
    sigma=10
    normalize=0.0
    nr,nc=f.shape[:2]
    filter1=np.array([[0,1,0],[1,-4,1],[0,1,0]])
    g=np.zeros((3,3),dtype="float")
    gradient1=np.zeros([nr,nc],dtype="uint8")
    edge=np.zeros([nr,nc],dtype="uint8")
    for x in range (3):
        for y in range (3):
            g[x,y]=np.exp(-(pow(x-2,2)+pow(y-2,2))/(2*pow(sigma,2)))
            normalize += g[x,y]
    for x in range (3):
        for y in range (3):
            g[x,y]=g[x,y]/normalize
    for r in range(1,nr-1,1):
        for c in range(1,nc-1,1): 
            temp1=0
            for x in range(3):
                for y in range(3):
                    temp1 += f[r-1+x,c-1+y]*filter1[x,y]*g[x,y]
            gradient1[r,c] = np.uint8(np.clip(temp1,0,255))
    for r in range(0,nr,1):
        for c in range(0,nc,1):
            if abs(gradient1[r,c])>T:
                edge[r,c]=255
    return edge
def main():
    img1=cv2.imread("car_plate.jpg",cv2.IMREAD_GRAYSCALE)
    img2=Marr_Hildreth(img1)
    cv2.imshow( "Original Image", img1 )	
    cv2.imshow( "composite laplacian", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
main()