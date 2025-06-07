a = 17 #int(input('1--> '))
b = 3 #int(input('2--> '))

if a>b:
    big = a
    #small = b
else:
    big = b
    #small = a
step = big
while True:
    if (big % a==0 and big% b==0):
        break
    else:
        big += step
        
print(big)