

from PIL import Image

im = Image.open('C:/Users/ahmet/Downloads/sinifDersler/bitirmePro/Konum.png')
px = im.load()
#görüntünün yükseklik ve genişlik değerinin alınması
w, h = im.size

#anahtar değerlerinin verilmesi
y0 = 1
x0 = 1.001
a = 1.4
b = 0.005
#yeni piksel kordinatlarını depolamak için boş bir liste
newpixel = []

for i in range(0, h * w):
    x = 1 - a * pow(x0, 2) + y0
    y = b * x0
    xr = int(('%.12f' % (x))[5:9]) % w
    yr = int(('%.12f' % (y))[5:9]) % h
    newpixel.append((xr, yr))
    x0 = float('%.14f' % (x))
    y0 = float('%.14f' % (y))

newpixel.reverse()
#piksellerin her biri için karıştırma yapacak dongu
for i in range(0, h * w):
    #yeni kordinatlar xr,yr ye atanır
    (xr, yr) = newpixel[i]
    
    j = h * w - i - 1
    p = px[j % w, int(j / w)]
    #pr xr yr deki yeni pikselin degerini alır
    pr = px[xr, yr]
    #
    px[j % w, int(j / w)] = pr
    #ifadesi orjinal pikselin değeriyle değiştirir 
    px[xr, yr] = p

im.save('C:/Users/ahmet/Downloads/sinifDersler/bitirmePro/22Ko.png')