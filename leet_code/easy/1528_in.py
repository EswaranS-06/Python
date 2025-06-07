#shuffling String
class Solution(object):
    def restoreString(self, string, indices):
        string = list(string)
        temp = [string[i] for i in indices]
        return "".join(temp)
       
test = Solution()
string = ["codeleet","abc"]
indices = [[4,5,6,7,0,2,1,3],[0,1,2]]

for y,x in zip(string, indices):
    print(test.restoreString(y, x))
