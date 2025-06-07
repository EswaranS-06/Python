class Solution(object):
    def rotateString(self, s, goal):
        s = list(s)
        if len(s) == len(goal):
            for i in range(len(s)):
                s.append(s.pop(0))
                if "".join(s) == goal:
                    return(True)
                
            else:
                return False
        else:
            return False    
        
        
test = Solution()
string = ["abcde","abcde"]
goal = ["cdeab","abced" ]

for y,x in zip(string, goal):
    print(test.rotateString(y, x))
