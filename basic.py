"""import calendar
year=int(input("enter a :"))
month=int(input("enter month:"))
cal=calendar.month(year,month)
print(cal)"""
"""year=int(input("enter a year:"))
if (year%400==0) and (year%100==0):
    print(f"{year }is leap")
elif (year%4==0) and (year%100!=0):
    print(f"{year} is leap")
else:
    print(f"{year} is not a leap")"""
"""num=int(input("enter a num: "))
if num==1:
    print(f"{num} is not a prime")
elif num>1:
    for i in range(2,num):
        if num%i==0:
            print(f"{num} is not a prime ")
            break
    else:
     
     print(f"{num} is prime number")"""
"""lower=1
upper=10
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)"""
'''def fib(n):
    a,b=0,1
    for i in range(n):
        print(a)
        a,b=b,a+b
fib(10)'''
"""def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
for i in range(10):
    print(fib(i))"""
def fact(n):
    res=1
    for i in range(1,n+1):
        res*=i
fact(5)
    




