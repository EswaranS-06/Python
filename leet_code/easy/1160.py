from typing import List

# Solution class
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d = {}
        index = -1
        for i in words:
            for j in i:
                for k in chars:
                    if k == j:
                        d.update({j:1})
                    else:
                        d.update({j:0})
                        
        res = 0 
        print(d)            
        for i in d.values():
            print(i)
                
        return res
                    
        # lst = []
        # index = -1
        # for i in chars:
        #     for j in words:
        #         index+=1
        #         lst.append(list())
        #         for k in j:
        #             if k == i:
        #                 lst[index].append(1)
        #             else:
        #                 lst[index].append(0)
                
        # res = 0              
        # for i in lst:
        #     print(i)
        #     if all(i):
        #         res+=sum(i)
                
        # return res


# ----------- Test harness for local testing -----------

def test_case_1():
    words = ["cat", "bt", "hat", "tree"]
    chars = "atach"
    expected = 6  # 'cat' and 'hat' can be formed (3 + 3)
    return words, chars, expected

def test_case_2():
    words = ["hello", "world", "leetcode"]
    chars = "welldonehoneyr"
    expected = 10  # 'hello' and 'world' can be formed
    return words, chars, expected

def run_test(words, chars, expected):
    sol = Solution()
    result = sol.countCharacters(words, chars)
    print(f"Words: {words}")
    print(f"Chars: '{chars}'")
    print(f"Expected: {expected}, Got: {result}")
    print("✅ Passed" if result == expected else "❌ Failed")
    print('-' * 40)

if __name__ == "__main__":
    # Run the tests
    for test_func in [test_case_1, test_case_2]:
        words, chars, expected = test_func()
        run_test(words, chars, expected)
