class Solution(object):
    def findTheDifference(self, s, t):
        res = ''
        t = list(t)
        for i in s:
            t.remove(i)
            
        return t.pop()
    
        
test=Solution()
print(test.findTheDifference("abcd","abcde"))