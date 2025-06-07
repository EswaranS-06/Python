class Solution(object):
    def merge(self, nums1, m, nums2, n):
        for i in range(m,len(nums1)):
            nums1[i]=nums2[0]
            nums2.pop(0)
            
        nums1 = nums1.sort()
            
        
test = Solution()
lst1 = [1,2,3,0,0,0]
m = 3
n = 3
lst2 = [2,5,6]

print(test.merge(lst1, m, lst2, n))