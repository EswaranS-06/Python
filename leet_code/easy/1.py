nums = [3,2,4]
target = 6

# for my undrstanding
'''lst = []
for i in nums:
    for j in nums:
        if (i + j) == target and j != i:
            lst.append(i)
            continue 
    continue

print(lst)
'''


'''
lst = [i for i in range(len(nums)) for j in range(len(nums)) if ( nums[i] + nums[j]) == target]

print(lst)

''' # <-- list comperhension


lst = []
for i in range(len(nums)):
    for j in range(len(nums)):
        if (nums[i] + nums[j]) == target and j != i:
            lst.append(i)
            continue 
    continue

print(lst)
 # <-- this is actual program