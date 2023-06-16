

#anahtarlama algoritmasının import edilmesi
import anahtarlama as antr
#gerekli kütüphanelerin entegre edilmesi
import matplotlib.pyplot as plt
import matplotlib.image as rdimg
import numpy as np
import cv2
#resim yolunun alınması
image = cv2.imread('C:/Users/ahmet/Downloads/sinifDersler/bitirmePro/Security.png')
#resmin gri tona çevrilmesi
resim = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.imshow(resim)
plt.show()

#resmin yükseklik degerinin alınması
height=resim.shape[0]
#resmin genişlik degerinin alınması
width=resim.shape[1]
#x değeri r değeri ve boyutun şifreleme fonksyonuna gönderilmesi
anahtar=antr.sifreleme(0.01,3.95,height*width)
print(anahtar)

z=0
# Satır ve sütunları sıfırlardan oluşan şifreliResim değişkeni
sifreliResim=np.zeros(shape=[height,width,4],dtype=np.uint8)
for i in range(height):
    for j in range(width):
        #şifreliResim değişkenine, resmin pixel değerleri ile oluşturulan anahtarlar XOR işleminden sonra yeni değerlerin şifreli resme atanması
        sifreliResim[i,j]=resim[i,j]^anahtar[z]
        #döngü sonunda z değerinin artması
        z+=1

print('sifreliResim')        
plt.imshow(sifreliResim)
plt.show()
#şifreli resmin kaydedilmesi
plt.imsave('C:/Users/ahmet/Downloads/sinifDersler/bitirmePro/EncryptedSecurity.png',sifreliResim)

