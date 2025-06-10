class Solution(object):
    def lexicalOrder(self, n):
        result = []

        def dfs(curr):
            if curr > n:
                return
            result.append(curr)
            for i in range(10):
                next_num = curr * 10 + i
                if next_num > n:
                    return
                dfs(next_num)

        for i in range(1, 10):
            dfs(i)

        return result

                    
    
t = Solution()
ns = [13,25,2,101]
for i in ns:
    print(t.lexicalOrder(i))