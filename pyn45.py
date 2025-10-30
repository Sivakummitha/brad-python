#write a recursive function that performs addition of first n numbers
def fun(n):
    if n==1:
        return 1
    else:
        return n+fun(n-1)
n=int(input("enter a number: "))
print(f"sum of {n} is {fun(n)}")
