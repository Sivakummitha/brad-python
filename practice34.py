n = 20
count = 0
num = 2
while count < n:
    prime = True
    for i in range(2, n):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num)
        count += 1

    num += 1
