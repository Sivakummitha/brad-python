p=float(input("enter principle:"))
r=float(input("enter rate of change of intrest: "))
t=float(input("enter time taken:"))


simple_intrest=p*t*r/100
compound_intrest=p*(1+r/100)**t-p
print(f'simple intrst is {simple_intrest}')
print(f'coumpound intrest is {compound_intrest}')