def fact(n):
    if n == 0:
        return sum
    print(n)
    if n!=0:
        fact(n)

#fact(5)

n, fact = 5, 1
while n!=0:
    n = n-1
    fact = fact * n
    print(fact, n)

'''names = ['rex', 'ram', 'roy', 'rani']
marks = [98, 50, 59, 67]

stu = {n:m for n, m in zip(names, marks)}
square = {x:x*x for x in range(1,20)}

print("sorted",sorted(stu.values()))
print(stu.get('rey'))

d1={1:11,2:22}
d2={3:33,4:44}
d2.update(d1)
print(d2)
'''