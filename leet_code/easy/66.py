digits = [1,2,3]
d = 0
for i in digits:
    d = i + d * 10
str1 = str(d + 1)    
lst = [int(i) for i in str1]

print(lst)