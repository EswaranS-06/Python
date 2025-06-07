from collections import Counter
class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        #s = len([i for i in stones if i in jewels])
        return len([i for i in stones if i in jewels])
        
test = Solution()
stones = ["aAAbbbb","ZZ"]
jewels = ["aA","z"]
for stone, jewel in zip(stones, jewels):
    print(test.numJewelsInStones(jewel, stone)) 