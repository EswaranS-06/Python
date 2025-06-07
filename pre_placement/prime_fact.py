def primefact(a):
    i = 2
    if(a==1):
        return
    while(a%i != 0):
        i = i + 1
    print(i,end="")
    primefact(a//i)
    
primefact(100)