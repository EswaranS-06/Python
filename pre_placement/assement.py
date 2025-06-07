def monkey(x,y,z):
        dis = 0
        c = 0
        while x >= dis:
            dis += y
            c += 1
            if x>=dis:
                dis -= z
                c += 1
        return c-2
            
print(monkey(30,10,5))
print(monkey(21,5,3))