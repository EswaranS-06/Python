'''def ram(n):
    for i in range(20):
        if(i%n == 3):
            return
        else:
            print("Hai!!!")
    print("Are you Okay")'''
    
'''def ram(n):
    if(n==4):
        return
    print(n+10)
    ram(n+1)
    print(n)'''
    
def raju(a):
    if(a==1):
        a=a-1
    raju(a)
    print('Hai!!!->',a)
    
#ram(1)
raju(5)