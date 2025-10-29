#Write a program to find n first prime numbers
n=int(input("enter a number: "))
count=0
num=2
while count<n:
    for i in range(2,n):
        if n%i==0:
            break
    else:
        print(num)
        count+=1
    num+=1
