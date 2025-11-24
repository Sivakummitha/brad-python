"""def fib(n):
    a,b=0,1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
    fib(10)

def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
for i in range(10):
    print(fib(i))
"""
"""def fact(n):
    facti=1
    for i in range(n):
        facti*=i
    print(facti)
fact(5)
def fact(n):
    if n==1:
        return n
    return n*fact(n-1)
print(fact(5))"""
num=153
digits=len(str(num))
sum=0
while num>0:
    digit=num%10
    sum+=digit**digits
    num//=10
if sum==sum:
    print(num)
