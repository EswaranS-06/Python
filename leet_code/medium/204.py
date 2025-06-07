class Solution(object):
    def countPrimes(self, n):
        isprime = [True] * n
        isprime[0] = isprime[1] = False
        i = 1
        while i * i < n:
            if isprime[i]:
                for j in range(i*i, n , i):
                    isprime[j]=False
            i += 1
        return  sum(isprime)                      
    
test = Solution()
testcases = [10,300,26,100,150]
for testcase in testcases:
    print(test.countPrimes(testcase))