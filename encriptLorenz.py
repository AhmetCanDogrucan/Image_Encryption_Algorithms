import Lorenz as kg
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np


img=mpimg.imread('C:/Users/ahmet/Downloads/sinifDersler/bitirmePro/Pepper.bmp')


plt.imshow(img)
plt.show()

height=img.shape[0]
width=img.shape[1]

#kg.LorenzKey işlevi çağrılarak Lorenz sistemi kullanılarak anahtar dizisi elde edilir. Başlangıç değerleri 0.01, 0.02 ve 0.03 olarak belirlenir. Diziler xkey, ykey ve zkey değişkenlerine atanır.
xkey,ykey,zkey=kg.LorenzKey(0.01, 0.02, 0.03, height*width)

l=0
x=[]
y=[]
#xkey ve xindex dizileri kullanılarak enimg dizisinin sütunları yeniden düzenlenir. Sütunlar, xkey dizisinin sıralamasına göre yeniden sıralanır.
xindex=[]
#ykey ve yindex dizileri kullanılarak enimg dizisinin satırları yeniden düzenlenir. Satırlar, ykey dizisinin sıralamasına göre yeniden sıralanır.
yindex=[]
enimg=np.zeros(shape=[height,width,4],dtype=np.uint8)
l=0
#width kadar bir döngü oluşturularak xindex listesine sıralı sayılar eklenir.
for i in range(width):
    xindex.append(i)
for i in range(height):
    #height kadar bir döngü oluşturularak yindex listesine 1 değeri eklenir.
    yindex.append(1)
#width kadar bir döngü oluşturulur. Bu döngü, xkey dizisinin sıralanması ve aynı sıralamayı xindex ve yindex listelerine uygulamak için kullanılır.
for i in range(width):
    for j in range(width):
        # Eğer xkey[i] değeri, xkey[j] değerinden büyükse, xkey[i] ve xkey[j] değerleri yer değiştirir. Aynı zamanda xindex[i] ve xindex[j],   
        if(xkey[i]>xkey[j]):
            xkey[i],xkey[j]=xkey[j],xkey[i]
            xindex[i],xindex[j]=xindex[j],xindex[i]
for i in range(height):
    for j in range(height):
        if(ykey[i]>ykey[j]):
            ykey[i],ykey[j]=ykey[j],ykey[i]
            #yindex[i] ve yindex[j] değerleri de yer değiştirir.  
            yindex[i], yindex[j]=yindex[j],yindex[i]

#height kadar bir döngü oluşturulur ve içinde k adında bir değişken tanımlanır. Bu döngü, enimg dizisini yeniden düzenlemek için kullanılır. 
for i in range(height):
    k=0
    for j in range(width):
        #Her satırda, img dizisindeki yindex[k] indisine sahip değerler, enimg dizisine kopyalanır ve k değeri artırılır.
        enimg[i][j]=img[yindex[k]][j]
        k=k+1
#height kadar bir döngü oluşturulur ve içinde k adında bir değişken tanımlanır. Bu döngü, enimg dizisinin her satırında xindex[k] indisine sahip değerlerin yeniden düzenlenmesi için kullanılır.
for i in range(height):
    k=0
    for j in range(width):
        # Her satırda, enimg[i] dizisindeki değerler, enimg[i][xindex[k]] indisine yerleştirilir ve k değeri artırılır.
        enimg[i][j]=enimg[i][xindex[k]]
        k=k+1
plt.imshow(enimg)
plt.show()
#l değişkeni sıfırlanır.
l=0
#height kadar bir döngü oluşturulur ve içinde width kadar bir döngü yer alır. Bu döngüler,
for i in range(height):
    for j in range(width):
        # her piksele XOR işlemi uygulamak için kullanılır. XOR işlemi için zkey dizisinin öğeleri, pow(10, 12) ile çarpılır, ardından 256'ya göre mod alınır ve tam sayıya dönüştürülür
        zk=(((zkey[l]*pow(10,12))%256).astype(int))
        #. Elde edilen değer, enimg[i, j] öğesiyle XOR işlemine tabi tutulur ve sonuç enimg[i, j] olarak atanır. l değeri artırılır.
        enimg[i,j]=enimg[i,j]^zk
        l+=1

plt.imshow(enimg)
plt.show()
plt.imsave('C:/Users/ahmet/Downloads/sinifDersler/bitirmePro/EncLorenzPepper.bmp',enimg)

        
        
        
        
            