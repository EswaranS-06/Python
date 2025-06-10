class Account():
    def __init__(self, ac, name, age):
        self.name = name
        self.ac = ac
        self.age = age
    
    def __str__(self):
        return f'''
    Name: {self.name}
    Age : {self.age}
    A/c no: {self.ac}
    
    '''
    
for i in range(1, 4):    
    lst = []
    name = input(f'{i}.Enter your name:')
    age = int(input(f'{i}.Enter your age:'))
    ac = int(input(f"{i}.Enter your A/c no:"))

    acc = Account(ac, name, age)
    lst.append(acc)

print(lst)