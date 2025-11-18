string=str(input("enter a string: "))
vowel="aeiou"
for ch in vowel:
    string=string.replace(ch,'*')
print(string)