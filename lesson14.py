import cv2
import numpy as np
from matplotlib import pyplot as plt
from numpy.lib.function_base import median

img=cv2.imread("lena.jpg")
#img=cv2.imread("water.png")
#img=cv2.imread("halftone_gaussian_blur.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
kernel=np.ones((5,5),np.float32)/25         # "K=[(1/25)x"birlerden oluşan matris]" olduğu için böyle yaptık

dst_Image=cv2.filter2D(img,-1,kernel)
blur_Image=cv2.blur(img,(5,5))
gsnblur_Image=cv2.GaussianBlur(img,(5,5),0)
mdnblur_Image=cv2.medianBlur(img,5)
bilateralFilter=cv2.bilateralFilter(img,9,75,75)    # Gürültü kaldırmada ve kenarları sivri tutmada çok etkili bir filtre

titles=["Original Image","Destination Image","Blured Image","Gaussian Blured Image","Median Blured Image","Bilateral Filter Image"]
images=[img,dst_Image,blur_Image,gsnblur_Image,mdnblur_Image,bilateralFilter]

for i in range(6):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()