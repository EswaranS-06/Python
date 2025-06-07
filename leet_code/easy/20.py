class Solution(object):
    def isValid(self, s):
        st = []
        b = {
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for i in s:
            if ( i in b.values()):
                st.append(i)
            else:
                if(not st or b[i]!=st.pop()):
                    return False

        return len(st) == 0
                 
testcase = ["([])","(]","()[]{}","()",'[','){']
test = Solution()
for i in  testcase:
    print(test.isValid(i))