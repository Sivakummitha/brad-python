import cmath

a = int(input("Enter a :"))
b = int(input("Enter b :"))
c = int(input("Enter c :"))
d = (b ** 2) - (4 * a * c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print("The solution of quadratic equations are :", sol1,sol2)