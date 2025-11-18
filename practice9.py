number=int(input("enter a number: "))
count=0
while number>0:
    number//=10
    count+=1
print(f"number of digits in number is{count}")
