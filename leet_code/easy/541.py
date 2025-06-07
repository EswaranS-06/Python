#Reverse String II
class Solution(object):
    def reverseStr(self, s, k):
        s = list(s)
        l = 0
        while l < k:
            s[l],s[k-1] = s[k-1],s[l]
            l += k
            k += k
            
        return "".join(s)
           
    
testcase = Solution()
srlst = ["abcdefg","abcd"]
k = 2
for sr in srlst:
    print(testcase.reverseStr(sr, k))