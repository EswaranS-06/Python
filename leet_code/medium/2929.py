class Solution(object):
    def distributeCandies(self, n, l):
        lst = [[i,j,k] for i in range(0,l+1) for j in range(0, l+1) for k in range(0, l+1) if i+j+k == n]

        return lst
                
        
test = Solution()
n = [5,3]
l = [2,3]
for i,j in zip(n,l):
    print(test.distributeCandies(i,j))