import random
a = [1, 2, 3, 4, 5, 6]
print(random.choice(a))
random.seed(5)
print(random.random())
print(random.random())
r1 = random.randint(5, 15)
print(r1)
r2 = random.randint(-10, -2)
print(r2)
a = [1, 2, 3, 4, 5, 6]
print(random.choice(a))
s = "sivacharan"
print(random.choice(s))
tup = (1, 2, 3, 4, 5)
print(random.choice(tup))
a = [1, 2, 3, 4, 5]
from random import sample
print(sample(a,3))
b = (4, 5, 6, 7, 8)
print(sample(b,3))
c = "143225"
print(sample(c,3))
import random
a = [1, 2, 3, 4, 5]
random.shuffle(a)
print("first: ",a)
random.shuffle(a)
print("Second: ",a)
random.shuffle(a)
print("third: ",a)



