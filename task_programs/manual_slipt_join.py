s = "0123456789"
c ='r'
print(s)
print(s[:5]+c+s[5+1:])
res = ""
for i in s:
    if ord(i) == 32:
        res+='-'
        
    else:
        res+=i
print(res)