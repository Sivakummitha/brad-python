#Write program to print first n fibonnacci numbers uisng Recursion technique
def fun(num):
    if num<=1:
        return 1
    else:
        return fun(num-1)+fun(num-2)
num=int(input("enter a number: "))
for i in range(num):
    print(fun(i))