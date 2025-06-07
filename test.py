import random

cus_dict = dict()
ac_no = random.randint(1000,9999)
cus_dict.update({6502:'acc'})
cus_dict.update({6532:'aii'})
cus_dict.update({6504:'att'})
cus_dict.update({6602:'arr'})
print(cus_dict.get(6503, "Not Found"))

'''a = 4**0.5
print(a)
'''

'''def add(*args):
    print(args, type(args))
    
add(10,20,30,40)'''



'''a = [[0,1,2],[0,1,2]]
a[0][0] = 20
print(a)'''
"""

mark = int(input("Enter the Marks"))
while mark != 0:
    if mark > 100:
        print("Invalid Mark")
    elif

"""



"""nums = [2, 7, 12, 13]
target = 9

lst = [i for i in range(len(nums)) for j in range(len(nums)) if ( nums[i] + nums[j]) == target]

print(lst)
"""

'''
lst = []
for i in range(len(nums)):
    for j in range(len(nums)):
        if (nums[i] + nums[j]) == target:
            lst.append(i)
            continue 
    continue

print(lst)
'''
