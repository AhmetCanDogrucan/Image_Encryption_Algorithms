
def sifreleme(a,b,boyut):
    
    anahtar=[]
    
    for i in range(boyut):
        
        a=b*a*(1-a)
        anahtar.append(int((a*pow(10,16))%256))
    return anahtar

