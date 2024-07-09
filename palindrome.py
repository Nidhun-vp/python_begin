import re

def is_palindrome(s):
    # 1. Remove non-alphanumeric characters from the input string.
    s = re.sub(r'[^a-zA-Z0-9]', '', s)
    
    # 2. Convert the cleaned string to lowercase.
    s = s.lower()
    
    # 3. Check if the cleaned and lowercase string is equal to its reverse.
    return s == s[::-1]

    
s=input("enter string:")
print(is_palindrome(s))
print(s)