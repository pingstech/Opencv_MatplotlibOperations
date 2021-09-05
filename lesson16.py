import cv2
import numpy as np
from matplotlib import pyplot as plt

def value1(temp):
    print("Low Value",temp)

def value2(temp):
    print("High Value",temp)

def value3(temp):
    print("Switch Position",temp)    

img=cv2.imread("messi5.jpg",0)

cv2.namedWindow("Canny")
cv2.createTrackbar("Low Value","Canny",0,255,value1)
cv2.createTrackbar("High Value","Canny",0,255,value2)
cv2.createTrackbar("ON / OFF Switch","Canny",0,1,value3)

lap=cv2.Laplacian(img,cv2.CV_64F,ksize=3)
lap=np.uint8(np.absolute(lap))
sobelX=cv2.Sobel(img,cv2.CV_64F,1,0)
sobelY=cv2.Sobel(img,cv2.CV_64F,0,1)
sobelX=np.uint8(np.absolute(sobelX))
sobelY=np.uint8(np.absolute(sobelY))

sobelCombined=cv2.bitwise_or(sobelX,sobelY)

while True:
    l_Val=cv2.getTrackbarPos("Low Value","Canny")
    h_Val=cv2.getTrackbarPos("High Value","Canny")
    switch_Pos=cv2.getTrackbarPos("ON / OFF Switch","Canny")

    if switch_Pos==0:
        canny=cv2.Canny(img,l_Val,h_Val)
        titles=["Image","Laplacian","SobelX","SobelY","Combined Sobel","Canny Image"]
        images=[img,lap,sobelX,sobelY,sobelCombined,canny]

        for i in range(6):
            plt.subplot(2,3,i+1)
            plt.imshow(images[i],"gray")
            plt.title(titles[i])
            plt.xticks([]),plt.yticks([])

        plt.show()

    else:
        plt.close('all')
        break