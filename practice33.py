n=int(input("enter a number: "))
for i in range(2,n):
    if n%i==0:
        print(f"the {n} is not a prime")
    else:
        print(f"rhe {n} is prime")
        