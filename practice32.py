year=int(input("enter year: "))

if (year%400==0)&(year%100==0):   
    print(f"the {year}is leap")
elif  (year%4==0)&(year%100!=0):
    print(f"the {year}is leap")
else:
    print(f"the {year} is not leap")