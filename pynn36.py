#Write a program to find whether a number is armstrong number or not
num=int(input("enter a number : "))
length_of_a_num=len(str(num))
num2=num
sum=0
while num2>0:
    digits=num2%10
    sum+=digits**length_of_a_num
    num2//=10
if num==sum:
    print('the number is armstrong')
else:
    print('the number is not a armstrong')