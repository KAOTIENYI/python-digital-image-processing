import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread( "gg123.jpg", -1 )
nr,nc=img.shape[:2]

if img.ndim == 3:
    hist=np.zeros([3,256],dtype ="uint16")
    color = ( 'b', 'g', 'r' )
    for i, col in enumerate( color ):
        for r in range (0,nr,1):
            for c in range (0, nc, 1):
                hist[i,img[r,c,i]]+=1
        plt.plot( hist[i], color =col )
plt.xlim( [0,256] )             # limitaton of x-axis
plt.xlabel( "Intensity" )       # label of x-axis
plt.ylabel( "#Intensities" )    # label of y-axis
plt.show( )


(b, g, r) = cv2.split(img)


cdf=np.zeros([256],dtype ="float")
cdf = hist[0].cumsum()
cdf = ((cdf)*255)/(nr*nc)
y = cdf.astype(np.uint8)
img4 = np.zeros((569, 850), dtype =np.uint16)
img4 = y[b]


cdf2=np.zeros([256],dtype ="float")
cdf2 = hist[1].cumsum()
cdf2 = ((cdf2)*255)/(nr*nc)
y2 = cdf2.astype(np.uint8)
img5 = np.zeros((569, 850), dtype =np.uint16)
img5 = y2[g]


cdf3=np.zeros([256],dtype ="float")
cdf3 = hist[2].cumsum()
cdf3 = ((cdf3)*255)/(nr*nc)
y3 = cdf3.astype(np.uint8)
img6 = np.zeros((569, 850), dtype =np.uint16)
img6 = y3[r]

img7 = np.zeros((569, 850,3), dtype =np.uint16)
img7 = cv2.merge([img4,img5,img6])


nr2,nc2=img.shape[:2]


if img7.ndim == 3:
    hist2=np.zeros([3,256],dtype ="uint16")
    color = ( 'b', 'g', 'r' )
    for i, col in enumerate( color ):
        for r in range (0,nr,1):
            for c in range (0, nc, 1):
                hist2[i,img7[r,c,i]]+=1
        plt.plot( hist2[i], color = col )
plt.xlim( [0,256] )             # limitaton of x-axis
plt.xlabel( "Intensity (After equalization)" )       # label of x-axis
plt.ylabel( "#Intensities" )    # label of y-axis
plt.show( )

cv2.imshow( "Original Image", img )	
cv2.imshow( "Histogram Equalization", img7)
cv2.waitKey(0)
