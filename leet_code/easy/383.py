# LeetCode 383 - Ransom Note
# File: ransom_note.py

class Solution:
    def canConstruct(self, r: str, magazine: str) -> bool:       
        for i in magazine:
            if i in r:
                temp = r[:r.find(i)]+r[r.find(i)+1:]
                r = temp
        
        return not bool(r)
                
                    

# ----------------- Local Test Code -----------------

def test_case(ransomNote, magazine, expected):
    sol = Solution()
    result = sol.canConstruct(ransomNote, magazine)
    print(f"ransomNote: '{ransomNote}', magazine: '{magazine}'")
    print(f"Expected: {expected}, Got: {result}")
    print("✅ Passed\n" if result == expected else "❌ Failed\n")

if __name__ == "__main__":
    # Add your test cases here
    test_case("a", "b", False)
    test_case("aa", "ab", False)
    test_case("aa", "aab", True)
    test_case("hello", "hleolworld", True)