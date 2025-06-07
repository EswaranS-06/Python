def s_p(n):
    """
    
    product = 1
    sum = 0
    lst = [int(i) for i in str(n)]
    for i in lst:
        product *= i
        sum += i
                
    print(product - sum)
    """
    sum = 0
    product = 1
    while n != 0:
        digit = n % 10
        sum = sum + digit
        product = product * digit
        n = n//10
        
    print(product - sum)
            
s_p(234)
"""s_p(47)
s_p(384765)
s_p(74)"""