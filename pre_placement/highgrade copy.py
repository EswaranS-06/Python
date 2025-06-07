n = ['rex73','ram28','ray95','rai57']
m = [73,28,95,57]

for i  in range(len(m)-1):
    for j in range(i+1,len(m)):
        if m[i] < m[j] :
            m[i],m[j] = m[j],m[i]
            n[i],n[j] = n[j],n[i]
            
print(n,"\n",m)