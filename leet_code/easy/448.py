#Find All Numbers Disappeared in an Array
class Solution(object):
    def findDisappearedNumbers(self, nums):
        print(nums)
        nums.sort()
        print(nums)
        lst = []
        for i in range(0, len(nums)):
            if  i+1 != nums[i]:
                lst.append(i+1)
        
        return lst
    
    def findDisappearedNumbers(self, nums):
        lst = [i for i in range(1,len(nums)+1)]
        
        return list(set(lst)^set(nums))
    
test = Solution()
lst = [4,3,2,7,8,2,3,1],[1,1],[1,2,3,4,4,4,7,7]
for i in lst:
    print(test.findDisappearedNumbers(i))