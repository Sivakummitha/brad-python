from functools import * 
@cache
def fun(n):
    if n<2:
        return n
    return fun(n-1)+fun(n-2)
print(fun(10))
print(fun(11))
@lru_cache(maxsize=5)
def add(a,b):
    return a+b
print(add(1,2))
print(add(2,3))
def sub(a,b):
    return a-b
print(sub(2,3))
print(sub(10,5))
def mul(a,b):
    return a*b
print(mul(10,2))
print(mul(20,3))
class functool:
    def show(self,a,b):
        print(a,b)
    half=partialmethod(show,50)
d=functool()
d.half(100)
nums=[1,2,3,4]
print(reduce(lambda x,y:x+y,nums))
@singledispatch
def display(value):
    print(value)
@display.register(int)
def _(value):
    print(value)
@display.register(list)
def _(value):
    print(value)
display(10)
display([1,2,3,4,5])

