num = int(input("Enter th number of Marks: "))
n=[]
m=[]
hn=[]
hm=[]
for i in range(num):
    n.append(input("Enter the Name of Stu: "))
    m.append(int(input("Enter the Marks of Stu: ")))

while len(n)!=0:
    h = m.index(max(m))
    hn.append(n[h])
    hm.append(m[h])
    n.pop(h)
    m.pop(h)
for i in range(len(hn)):
      
    print(f'{i+1} Mr/Mrs {hn[i]} has scored {hm[i]}')
    
