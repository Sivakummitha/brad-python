#write a program that contains fucntions argument pass by reference, pass by value, anonymous function, function in function
#1
def arg_pass_value(n):
    n=n+5
    print(n)
a=10
arg_pass_value(a)
print(a)
#2
def arg_pass_reference(list):
     return list
list_2 = ["x"]
arg_pass_reference(list_2)
print(list_2)
#3
square=lambda x:x*x
print(square(10))
#4
def fun1(msg):
    def fun2():  
        print(msg)
    fun2()
fun1("hello! sivacharan")



