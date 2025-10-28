#Write a program that includes all types of conditions - , if, if else, if elif, nested if , Short Hand If, Short Hand If  Else, Ternary operator
a = 10
b = 20
c = 5
if a < b:
    print(" b is greater than a")
if a > b:
    print(" a is greater than b")
else:
    print(" b is greater than a")
if a > b:
    print(" a is greater")
elif a == b:
    print(" both are equal")
else:
    print(" b is greater")
if a < b:
    if a < c:
        print("a is smallest")
    else:
        print("a is smaller than b but not smallest")
if a < b: print(" b is greater")
print("short hand if else:", "a is greater" if a > b else "b is greater")
result = "Equal" if a == b else "Not Equal"
print("ternary operator:", result)