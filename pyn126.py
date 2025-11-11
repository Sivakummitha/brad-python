#I reffered from chatgpt and i understood the logic then i proceeded the program with my own
import numpy as np
from scipy.optimize import root,linprog
print("ROOT FINDING EXAMPLE")
def f(x):
    return x**3-5*x+3
sol=root(f,0)
print("Root of equation:",sol.x)
print("Success:",sol.success)
print()
print("LINEAR PROGRAMMING EXAMPLE")
c=[3,2]
A=[[1,2],[3,2]]
b=[6,12]
res=linprog(c,A_ub=A,b_ub=b,bounds=(0,None))
print("Optimal values (x1,x2):",res.x)
print("Minimum cost:",res.fun)
