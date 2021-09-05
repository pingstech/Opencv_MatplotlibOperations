import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread("lena.jpg")
cv2.imshow("Lena Image",img)

img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # Bu işlemi yapmadan aşağıdaki işleme geçmememiz gerekiyor. Eğer yaparsak
plt.imshow(img)                         # Resmi, matplotlib'in formatı "RGB" ve cv2'nin formatı da "BGR" olduğundan farklı renkli bir görüntü görücez
plt.xticks(np.arange(0,512,32))         # Burada bu işlemle X düzlemine 0'dan, 512'ye kadar 32 artacak şekilde aralıklar verdik
plt.yticks(np.arange(0,512,16))         # Burada bu işlemle y düzlemine 0'dan, 512'ye kadar 16 artacak şekilde aralıklar verdik
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()