x = -1203
sign = -1 if x < 0 else 1
x = abs(x)
rev = 0
while x > 0:
    rev = rev * 10 + (x % 10)
    x //= 10
rev *= sign
print("reversed:", rev)
