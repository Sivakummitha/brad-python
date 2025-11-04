def div_sum(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s
limit = int(input("Enter limit: "))
total = 0
for a in range(2, limit):
    b = div_sum(a)
    if b != a and div_sum(b) == a and b < limit:
        total += a
print("Sum of amicable numbers:", total)
