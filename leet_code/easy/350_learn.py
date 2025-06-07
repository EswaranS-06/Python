from collections import Counter
class Solution(object):
    def intersect(self, nums1, nums2):
        
        c1 = Counter(nums1)
        c2 = Counter(nums2)
        
        res = []
        for i in c1 & c2:
            res.extend([i] * min(c1[i], c2[i]))
            
        return res
        
              
test = Solution()
x_s = [[1,2,2,1], [4,9,5]]
y_s = [[2,2], [9,4,9,8,4]]
for x, y in zip(x_s, y_s):
    print(test.intersect(x, y))