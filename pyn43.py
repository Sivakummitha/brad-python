#"Write a Python function to check whether a number is perfect or not.
#Example : The first perfect number is 6, because 1, 2, and 3 are its proper positive divisors, and 1 + 2 + 3 = 6. Equivalently, the number 6 is equal to half the sum of all its positive divisors: ( 1 + 2 + 3 + 6 ) / 2 = 6. The next perfect number is 28 = 1 + 2 + 4 + 7 + 14. This is followed by the perfect numbers 496 and 8128."
def perfect_number(num):
    if num<=0:
        return False
    sum=0
    for i in range(1,num+1):
        if num%i==0:
            return True
        sum+=1
    return sum==num
num1=perfect_number(6)
num2=perfect_number(28)
num3=perfect_number(496)
num4=perfect_number(8128)
print(num1)
print(num2)
print(num3)
print(num4)
