def is_palindrome(text):
    #rev_text = text.lower().replace(" ","")[::-1]
    text = text.lower().replace(" ","")[::-1] #<-- by me
    rev_text = text[::-1]
    return rev_text == text
    """clean_text = ''.join(filter(str.isalnum, text.lower()))""" #<-- by chatgpt
    """return clean_text == clean_text[::-1]"""
    

text = "Race car" #input("Enter the String: ")
str1 = "Able was I ere I saw Elba"
str2 = "Helloo"
print(is_palindrome(text))
print(is_palindrome(str1))
print(is_palindrome(str2))
