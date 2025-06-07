str1 = "RAJU"
str2 = "PAVI"
str1 = str1.lower()
str2 = str2.lower()
lst1 = [i for i in str1]
lst2 = [j for j in str2]


for i in range(len(lst1)):
    for j in range(len(lst2)):
        if lst1[i]==lst2[j]:
            lst1[i]='/'
            lst2[j]='/'
            
count1 = len(lst1)-lst1.count("/")
count2 = len(lst2)-lst2.count("/")
total = count1 + count2   

ans = ["F","L","A","M","E","S"]
 
f = 0
while(len(ans)!=1):
    f=(f+(total-1))%len(ans)
    ans.pop(f)
    
print(ans)