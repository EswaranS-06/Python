num = 14
count =  0
while num != 0:
    if num%2 == 0:
        num = num/2
        #count = count + 1

    else:
        num -= 1
        #count = count + 1
    count = count + 1
        
print(count)