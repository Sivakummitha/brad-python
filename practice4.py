num1=int(input("enter a number1: "))
num2=int(input("enter a number2: "))
num3=int(input("enter a number3: "))
if num1>=num2&num1>=num3:
    print(f"{num1} is largest")
elif num2>=num1&num2>=num3:
    print(f"{num2} is largest")
else:
    print(f"{num3} is largest")
#method2
a=int(input("enter a number1: "))
b=int(input("enter a number2: "))
c=int(input("enter a number3: "))
print(max(a,b,c))
