"""print("hello world!")
a=10
b=20
c=a+b
print("sum of a and b is: ",c)"""
import cmath
a=float(input("enter a: "))
b=float(input("enter b: "))
c=float(input("enter c: "))
discriment=b**2-4*a*c
if discriment>0:
    root1=(-b+cmath.sqrt(discriment))/(2*a)
    root2=(-b-cmath.sqrt(discriment))/(2*a)
    print("root1 is: \n",root1)
    print("root2 is: \n",root2)
elif discriment==0:
    root=-b/2*a
    print("root is :",root)
else:
    real_part=-b/2*a
    imaginary_part=cmath.sqrt(discriment)/(2*a)
    print(f"{real_part}+{imaginary_part}*i and {real_part}-{imaginary_part}*i")
    
    
