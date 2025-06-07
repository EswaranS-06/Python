n = 5#int(input("Enter the no: "))
c = 0
for i in range(1,n+1):
    
    for j in range(1,i+1):
        c = c +  i
        print(c,end=" ")

    print("")

'''mark = 1
total = 0
count = 0
while mark != 0:
    mark = int(input("Enter the Marks: "))
    if mark <= 100 and mark > 40:
        print(f"Valid Mark: {mark}")
        total = mark + total
        count = count + 1
        
    else:
        
        print(f"Invalid Mark: {mark}")
        
    avg = total/count
    
print(avg)'''