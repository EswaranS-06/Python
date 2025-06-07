class Solution(object):
    def isAnagram(self, s, t):
        a = sorted(list(i for i in s))
        b = sorted(list(i for i in t))
        
        
        return a == b
            
           
S = ["anagram","rat","care"]
T = ["nagaram","car","race"]
test = Solution()
print(test.isAnagram(S[0],T[0]))
print(test.isAnagram(S[1],T[1]))
print(test.isAnagram(S[2],T[2]))