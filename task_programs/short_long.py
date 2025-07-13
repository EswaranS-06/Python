no = int(input("No of Names: "))
large = 0
small = 0
names = []
for i in range(1,no+1):
    name=input(f"Enter the {i} Name: ")
    names.append(name)
    if len(name) > large:
        large = len(name)
    elif len(name) < small:
        small = len(name)
    else:
        small = len(name)
        
print([name for name in names if len(name) == large])
print([name for name in names if len(name) == small])