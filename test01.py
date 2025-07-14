import time
import os
print("""lst = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
lst.pop(4)
lst.append(lst.pop())
print(lst)""")
time.sleep(2)
os.system('cls')
while True:
    print("screen clear")
    input()
# c = 2
# s = 2
# lst = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
# lst1 = [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
# for i in lst:
#     print(f"\n{i}:")
#     for j in lst:
#         if i==j:
#             print(f"({j} {(i+j)} = {(i+j)>>1})", end=", ")
#             continue
#         print(f"{j}  {(i+j)} = {(i+j)>>1}", end=", ")
# from random import randrange as r
# from time import sleep as s
# while True:
#     a = r(2,5,2)
#     a = r(2,5,2)
#     print(a)

# def fact(n):
#     if n == 0:
#         return sum
#     print(n)
#     if n!=0:
#         fact(n)

# #fact(5)

# n, fact = 5, 1
# while n!=0:
#     n = n-1
#     fact = fact * n
#     print(fact, n)

# '''names = ['rex', 'ram', 'roy', 'rani']
# marks = [98, 50, 59, 67]

# stu = {n:m for n, m in zip(names, marks)}
# square = {x:x*x for x in range(1,20)}

# print("sorted",sorted(stu.values()))
# print(stu.get('rey'))

# d1={1:11,2:22}
# d2={3:33,4:44}
# d2.update(d1)
# print(d2)
# '''