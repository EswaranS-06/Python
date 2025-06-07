class Solution(object):
    def singleNumber(self, nums):
        
        numset = list(set(nums))
        nt=sum(nums)
        st=sum(numset)*2
        return st - nt
        """
        :type nums: List[int]
        :rtype: int
        """
        
test = Solution()
testcases = [[4,1,2,1,2],[2,2,1]]
for testcase in testcases:
    print(test.singleNumber(testcase))