n = 6
s = '1' #<----initializing s as 1 because it's always starts at 1 for now i am using it out of the while 
while n!=1: 
    
    lst = []  # <---- empty list to apppend the for loop output
    c = 1  #<---- logic is 'for loop' iterate one item that point if condition becomes else->else, so c = 1
    for i in range(len(s)):  #<---- for loop to tarvel by index
        j = i + 1     #<---- using j instant of using i + 1 in multiple place 
        
        if j >= len(s):   #<--- at one point the i+1 above the len to avoid that index error 
            lst.append(str(c))
            lst.append(s[i])
        else:
            if s[i] == s[j]:  #<--- if both i and j is equal i am addig one to the count 
                c += 1            
            else:     #<----- at one point the i!=j so i am appending that c and string index
                lst.append(str(c))
                lst.append(s[i])
                c = 1      #<---- and resetting the c = 1 because that means there is no more same value
    n -= 1
    s = (''.join(str(i) for i in lst))
    
print(s)