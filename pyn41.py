#Write a program that contains different types of functions and calling such as default arguments, keyword arguments and variable lenght argument and mixed arguments
#positional arguments
def add(a,b):
    print(a+b)
add(10,20)
#keyword arguments
def add(a,b):
    print(a+b)
add(a=20,b=10)
#default arguments
def fun(name='siva'):
    print(name)
fun()
#variable length arguments
def add(*numbers):
    total=0
    for i in numbers:
        total+=i
    print(total)
add(10,20,30,40,50)

