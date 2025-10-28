#Write a program to generate a random password that contains Upper, lower, numeric and special chars(@, #, $ and underscore
import random
upper_let="ABCDEFGHIJKLMNOPQRSTUVXYZ"
lower_let="abcdefghijklmnopqrstuvxyz"
numeric="0123456789"
spec_char="@#$_"
all=upper_let+lower_let+numeric+spec_char
password_length=int(input("enter a length:"))
password=[]
password.append(random.choice(upper_let))
password.append(random.choice(lower_let))
password.append(random.choice(spec_char))
password.append(random.choice(numeric))
for i in range(password_length-4):
    password.append(random.choice(all))
    random.shuffle(password)
final_password="".join(password)
print("password:",final_password)

