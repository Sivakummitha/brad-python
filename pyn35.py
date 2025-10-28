#Write program to print first n fibonnacci numbers uisng Recursion technique
def fib(num):
    if num<=1:
        return num
    else:
        return fib(num-1)+fib(num-2)
num=int(input("enter a number: "))
for i in range (num):
    print(fib(i))
        