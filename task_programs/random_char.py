import random as r
c = []
for i in range(65, 91):
    c.append(chr(i))
    
for i in range(97, 123):
    c.append(chr(i))
        
print(c)
print(r.shuffle(c))
print(c)