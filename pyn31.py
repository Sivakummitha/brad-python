#Write a program that includes all types of loops - for, while, do while pass, break and continue
print("For Loop")
for i in range(1, 6):
    print(i)

print("While Loop")
i = 1
while i <= 5:
    print(i)
    i += 1

print("Do While Loop")
x = 1
while True:
    print(x)
    x += 1
    if x > 5:
        break

print("Break")
for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("Continue")
for i in range(1, 8):
    if i == 4:
        continue
    print(i)

print("Pass")
for i in range(1, 6):
    if i == 3:
        pass
    