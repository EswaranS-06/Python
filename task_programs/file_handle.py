with open("pf/demo.txt", '+r') as file:
    for i in file.readlines():
        print(i)
        
with open("pf/demo.txt", 'r') as file:
    for i in file.readlines():
        print(i)
file.close()