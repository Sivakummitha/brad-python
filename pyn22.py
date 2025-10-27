def is_palindrome(s):
    return s == s[::-1]
string1 = "madam"
string2 = "hello"

print(f"'{string1}' is a palindrome: {is_palindrome(string1)}")
print(f"'{string2}' is a palindrome: {is_palindrome(string2)}")
def is_symmetrical(s):
    n = len(s)
    if n % 2 != 0:  
        return False
    mid = n // 2
    first_half = s[:mid]
    second_half = s[mid:]
    return first_half == second_half
string3 = "yoyo"
string4 = "python"
string5 = "racecar" 
print(f"'{string3}' is symmetrical: {is_symmetrical(string3)}")
print(f"'{string4}' is symmetrical: {is_symmetrical(string4)}")
print(f"'{string5}' is symmetrical: {is_symmetrical(string5)}")