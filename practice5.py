character=str(input("enter a character:"))
vowels=['a','e','i','o','u']
if character in vowels:
    print(f"{character} is vowel")
else:
    print(f"{character} is consonants")