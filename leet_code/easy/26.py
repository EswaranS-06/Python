class Solution(object):
    def removeDuplicates(self, nums):
        nums = set(nums)
        nums = list(nums)
        le = len(nums)
        return nums, le
        #nums = []
        '''du = []
        i = 0
        while True:
            j = i + 1
            if j == len(nums):
                break
            elif nums[i] == nums[j]:
                du.append(nums.pop(j))
                #nums.append(temp)
                continue
            else:
                i+=1
                continue
            
        print(nums, len(nums), du)'''
        
        
        
t = Solution()
lst = [[1,1,2],[0,0,1,1,1,2,2,3,3,4]]
for i in lst:
    print(t.removeDuplicates(i))