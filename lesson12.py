import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("sudoku.png")
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

_,th1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
_,th2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
_,th3=cv2.threshold(img,255,255,cv2.THRESH_TRUNC)
_,th4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
_,th5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

titles=["Original Image","Binary Threshold","Inverse Binary Threshold","Trunc Threshold","To Zero Threshold","Inverse To Zero Threshold"]
images=[img,th1,th2,th3,th4,th5]

for i in range(6):
    plt.subplot(2,3,i+1)            # İlk parametre satır, ikinci parametre sütun ve üçüncüde indeks için
    plt.imshow(images[i])           
    plt.title(titles[i])

plt.show()