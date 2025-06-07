nums = []
co_1=[]
co_2=[]
co_3=[]

def factor(n_max, num):
    lst = []
    for j in range(2,n_max):
        if num%j==0:
            lst.append(j)
    return lst

nums = [int(input(f"Enter The Numbers {n}: ")) for n in range(3)]
for n in range(3):
    nums.append(int(input("Enter The Numbers: ")))
print(nums)

max_num = max(nums)

#fun call
co_1 = factor(max_num, nums[0])
co_2 = factor(max_num, nums[1])
co_3 = factor(max_num, nums[2])
 

#condition to 
print("----------------------------------")            
if((co_1 in co_2) or (co_2 in co_3) or (co_3 in co_1)):
    print("It`s Co-Prime")
else:
    print("It`s not Co-Prime")
