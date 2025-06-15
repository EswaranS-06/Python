s = "Hello!!!"
c = ''
for i in s:
    if i.isupper():
        c+=i.lower()
    else:
        c+=i.upper()
        
        
print(c)