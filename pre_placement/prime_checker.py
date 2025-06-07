def IsPrime(num):
    for i in range(2,num):
        if num%i == 0:
            return 0
    return 1

def Sum(nums):
    tot = [int(i) for i in str(nums)]
    return sum(tot)

    
for nums in range(100,1000):
    if IsPrime(nums) and IsPrime(Sum(nums)):
        print(nums)
