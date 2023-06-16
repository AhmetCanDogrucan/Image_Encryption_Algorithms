
#lojistik anahtarlama algoritmasının entegre edilmesi
import anahtarlama as antr
#gerekli kütüphanelerin entegre edilmesi
import matplotlib.pyplot as plt
import matplotlib.image as rdimg
import numpy as np
import cv2

#şifreli Resmin cv2 kütüphanesi ile okunması
image = cv2.imread('C:/Users/ahmet/Downloads/sinifDersler/bitirmePro/sifreli21223.png')
#sifreli Resmin gri tona çevrilmesi
resim = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Şifreli resmin yükseklik değerinin alınması
height=resim.shape[0]
#şifreli resmin genişlik değerinin alınması
width=resim.shape[1]
#şifreyi çözmek için gerekli olan yükseklik genişlik ve boyut değerleri
anahtar=antr.sifreleme(0.01,3.95,height*width)


z=0
# sütun ve satır değerleri 0'lardan oluşan şifreCozulmusResim adında bir değişken
sifreCozulmusResim=np.zeros(shape=[height,width,4],dtype=np.uint8)
for i in range(height):
    for j in range(width):
        #z değişkeni ile döngü boyunce alınan anahtar değerleri ile şifreli resim piksel değerleri XOR işlemi uygulanarak çözulmusResim değişkenine atanarak yeni değerler elde edilir
        sifreCozulmusResim[i,j]=resim[i,j]^anahtar[z]
        z+=1
print('cozulmus resim')
#piksel değerleri çözülmüş gerekli x ve r değerleri ile çözülmüş resim
plt.imshow(sifreCozulmusResim)
plt.imsave('C:/Users/ahmet/Downloads/sinifDersler/bitirmePro/Cozulmus1221.png',sifreCozulmusResim)
