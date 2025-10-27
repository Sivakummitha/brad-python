#Test if List contains elements in a given Range
list=[1,29,25,36,2,3,15]
low=int(input("enter lower range: "))
high=int(input("enter heigher range: "))
for n in list: 
  
  if low<=n<=high:
    print(n)