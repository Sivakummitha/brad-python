#Write a program to accept a string and count the frequency of each vowel.
string=input("enter a string: ")
vowel=['a','i','e','o','u']
frequency=[]
for i in vowel:
    count=string.count(i)
    frequency.append(count)
print(vowel)
print(frequency)