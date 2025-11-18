#method1
n=int(input("enter a number: "))
a,b=0,1
for i in range(2,n):
    c=a+b
    print(c)
    a=b
    b=c
#method2
def fib(n):
    a,b=0,1
    print(a,b,end=' ')
    for i in range(2,n):
        c=a+b
        print(c,end=" ")
        a,b=b,c
n=int(input("enter a number: "))
