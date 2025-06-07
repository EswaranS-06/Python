def conv(a):
    a = a.upper()
    a = list(a)
    a[0] = a[0].lower()
    a = ''.join(a)
    
    print(a) 
    
a = ['rahuL','MAX','EsWaraN']
for i in a:
    conv(i)