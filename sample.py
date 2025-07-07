d = {1:1, 2:3}
if not (d.get(3)):
  d.update({2:d.get(2)+1})
print(d)
# n = 'Eswa ARN  sss'
# lst = n.split(' ')
# bs = ''
# for i in lst:
#   if len(bs) < len(i):
#     bs = ''.join(i)
    
# print(bs)
# print()
'''
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
thislist.clear()
print(thislist)'''


'''a = '0123456789'
print(a[1])
print(a[2:])
print(a[2:5])
print(a[2:6:2])
print(a[-1])
print(a[-7:-1])
print(a[-7:-1:2])
print(a.strip('1'))

age = '36'
txt = "My name is John, I am " + age
print(txt)'''

'''def fact(n):
    if n == 1:
        return 2
    else:
      b = fact(n - 1)
      print("hai")
      return b + 1
      
    
print(fact(5))
'''
'''print(1+2+3+4+5+6+7+8+9+10+11+12+13+14+15+16+17+18+19)'''

"""a = 10
for i in range(1,20):
  if(i%2==0):
    continue
  else:
    while(True):
      a=a+2
      if(a%10==0):
        break
print(a)
"""
'''
D = { 5 :  {'P': {5: 'P'}, 6: 'Q'}, 7: 'R', 'Q':'S', "S": "T"}

print(D[D[D[5][6]]])

'''
"""
print(dict(sorted(s.items() ,key=lambda x: x[1]))) #use to order the dict value 


setl = {1,2,3,4}
set2 = (4,5)
set3 = (2,3,4,5,7,8)
print (setl.union(set2).intersection(set3))

def hello():
    print("Hello i am Sample.py")"""
    
"""a = [1,2,3,4]
b = [5,6,7,8]


c = (1,2,3,4,6)
d = (47,33,423)
m1 = a + b # m1
m2 = [list(a),b] # m2
b += a
t1 = c
print(m2)

d += c

s1 = {456,123,789,29}
l1 = [4,5,6]
t1 = (7,8,9)
ls1, s2 = {13,1,2}, {34,236,24,29}
s1.update(l1)

car = {"model" : 'car',"no" : 8264}
 
#set3 = ls1 + s2

print(l1)
print(s1|s2, s1&s2, s1^s2)
print(car['no'])
print(car.get('no')) 
x = {'type' : 'fruit', 'name' : 'apple'}
myset = {'apple', 'banana', 'cherry'}
for x in myset:
  print(x)
  
x.copy()"""

