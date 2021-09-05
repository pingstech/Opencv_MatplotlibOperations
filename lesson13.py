import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("smarties.png",cv2.IMREAD_GRAYSCALE)
#------------------HEPSİ AYNI İŞLEM------------------
#img=cv2.imread("smarties.png")
#img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#----------------------------------------------------

_,mask=cv2.threshold(img,220,255,cv2.THRESH_BINARY_INV)
kernal=np.ones((5,5),np.uint8)                                  # "dilate" işlemi için 2x2'lik bir matris oluşturduk
dilation=cv2.dilate(mask,kernal,iterations=2)                   # "cv2.dilate(kaynak,kernal)" şeklinde doldurulur, "kernal" bizim kaynağa uyguladığımız bir kare veya bir şekle sahip olan bir şey
                                                                # Bunun ile isdeğimiz kısmın daha net gözükmesini sağlıyoruz
erosion=cv2.erode(mask,kernal,iterations=1)                     # "dilate" işleminin tersi diyebiliriz
opening=cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernal)    
closing=cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernal)           # Daha iyi bir sonuç almak için kullandık  
mg=cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernal)                          
th=cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernal)

titles=["Original Image","Mask Image","Dilation Image","Erosion Image","Opening Image","Closing Image","Gradient Image","Tophat Image"]
images=[img,mask,dilation,erosion,opening,closing,mg,th]

for i in range(8):
    plt.subplot(2,4,i+1)
    plt.imshow(images[i],"gray")
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()