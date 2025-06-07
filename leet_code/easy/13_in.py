class Solution(object):
    def romanToInt(self, s):
        res = 0
        prev = 0
        roman = {'M':1000,'CM':9000,'D':500,'CD':400,'C':100,'XC':90,
         'L':50,  'XL':40,  'X':10, 'IX':9,  'V':5,  'IV':4, 'I':1    }
        for i in s[::-1]:
            if roman[i] >= prev:
                res += roman[i]
                
            else:
                res -= roman[i]
            prev = roman[i]
            
        return res
            
            
        
test = Solution()
testcases = ["III","LVIII","MCMXCIV"]
for testcase in testcases:
    print(test.romanToInt(testcase))
    
'''
I = 1
II = 2
III = 3
IV = 4
V = 5
IX = 9
X = 10

'''

