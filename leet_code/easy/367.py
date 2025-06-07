class Solution(object):
    def isPerfectSquare(self, num):
        return  num**0.5%1
    
test = Solution()
lst = [16,14,7,4]
for i in lst:
    print(test.isPerfectSquare(i))