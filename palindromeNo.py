def is_palindrome(n):
    num_str=str(n)
    return num_str==num_str[::-1]

num=12321
result=is_palindrome(num)
print(result)