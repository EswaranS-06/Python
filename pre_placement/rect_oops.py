class rect:
    def dim(self, l,b):
        self.l = l
        self.b = b
    def area(self):
        print(self.l*self.b)
        
lst = []
n = 3 #int(input("Enter : "))
for i in range(n):
    r = rect()
    l = 10+i#int(input(f"Enter L {i}:"))
    b = 10+i#int(input(f"Enter B {i}:"))
    r.dim(l,b)
    lst.append(r)
    
for i in range(n):
    print(f"Rect {i+1}")
    lst[i].area()
    print("-----------------\n")