def isPalindrome( x):
    strx=str(x)
    revx = strx[::-1]
    is_palindrome = revx == strx
    return is_palindrome

print(isPalindrome(-121))
print(isPalindrome(121))
print(isPalindrome(21))
print(isPalindrome(999))
print(isPalindrome(55))
print(isPalindrome(10101))