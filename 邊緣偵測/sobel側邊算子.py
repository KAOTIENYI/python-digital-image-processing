import numpy as np
import cv2


def composite_laplacian(f):
    T=150
    filter_y=np.array([[-1,-2,-1],[0,0,0],[1,2,1]])
    filter_x=np.array([[-1,0,1],[-2,0,2],[-1,0,1]])
    nr,nc=f.shape[:2]
    gradient_y=np.zeros([nr,nc],dtype="uint8")
    gradient_x=np.zeros([nr,nc],dtype="uint8")
    edge=np.zeros([nr,nc],dtype="uint8")
    for r in range(1,nr-1,1):
        for c in range(1,nc-1,1):
            tempx=0
            tempy=0
            for x in range(3):
                for y in range(3):
                    tempx += f[r-1+x,c-1+y]*filter_x[x,y]
                    tempy += f[r-1+x,c-1+y]*filter_y[x,y]
            gradient_x[r,c] = np.uint8(np.clip(tempx,0,255))
            gradient_y[r,c] = np.uint8(np.clip(tempy,0,255))
    cv2.imshow("X-axis Gradient",gradient_x)
    cv2.imshow("Y-axis Gradient",gradient_y)
    for r in range(0,nr,1):
        for c in range(0,nc,1):
            if abs(gradient_x[r,c])+abs(gradient_y[r,c])>T:
                edge[r,c]=255
    return edge
def main():
    img1=cv2.imread("car_plate.jpg",cv2.IMREAD_GRAYSCALE)
    img2=composite_laplacian(img1)
    cv2.imshow( "Original Image", img1 )	
    cv2.imshow( "composite laplacian", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
main()