#Check if a value exists in a dictionary and  Sort Python Dictionaries by Key or Value
dict={'a':10,'b':20,'c':15,'d':25}
value=int(input("enter a number: "))
if value in dict.values():
    print(f"{value} exists")
else:
    print(f"{value} doesnot exists")
print(sorted(dict))

