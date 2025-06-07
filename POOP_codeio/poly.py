class father:
    """def __init__(self,name,age):
        self.name=name
        self.age=age"""
    def show(self):
        print(self.name,self.age)

    def hello(self):
        print("hello from father")

class son(father):
    """def __init__(self,name,age,fathername):
        super().__init__(name,age)
        self.fathername=fathername"""

    def hello(self):
        print("hello by child")

f1 = father()
f1.hello()

c1 = son()
c1.hello()