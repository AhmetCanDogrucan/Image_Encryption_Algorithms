import PIL as pl

im = pl.Image.open('C:/Users/ahmet/Downloads/sinifDersler/bitirmePro/22Ko.png')
px = im.load()
w, h = im.size

#şifrenin doğru çözülmesi için gereken degerler
y0 = 1
x0 = 1.0000001
"""
Flattening to linear using one loop
"""
for i in range(0, h * w):
    x = 1 - 1.4 * pow(x0, 2) + y0
    y = 0.3 * x0
    x0 = float('%.14f' % (x))
    y0 = float('%.14f' % (y))
    xr = int(('%.11f' % (x))[5:9]) % w
    yr = int(('%.11f' % (y))[5:9]) % h

    p = px[i % w, int(i / w)]
    pr = px[xr, yr]
    px[i % w, int(i / w)] = pr
    px[xr, yr] = p

im.save('C:/Users/ahmet/Downloads/sinifDersler/bitirmePro/22Kob.png', optimize=False, progressive=False, quality=100)