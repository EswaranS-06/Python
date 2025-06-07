class sim:
    def cir(self):
        print(self.l*self.b )
    def set_dim(self,l,b):
        self.l = l
        self.b = b
    def d_l(self):
        print(self.l)
        
    def d_b(self):
        print(self.b)

s = sim()
s.set_dim(10,20)
s.d_l()
s.d_b()
s.cir()