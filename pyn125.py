#I reffered from chatgpt and i understood the logic then i proceeded the program with my own
import numpy as np
from scipy.optimize import minimize, curve_fit
print("OPTIMIZATION EXAMPLE")
def func(x):
    return x[0]**2+x[1]**2+2*x[0]+4*x[1]+4
x0=[0,0]
result=minimize(func,x0)
print("Minimum point:",result.x)
print("Minimum value:",result.fun)
print("Success:",result.success)
print()
print("CURVE FITTING EXAMPLE")
x_data=np.linspace(0,4,20)
A_true,B_true,C_true=2.5,1.3,0.5
y_data=A_true*np.exp(-B_true*x_data)+C_true+0.2*np.random.normal(size=len(x_data))
def model(x,A,B,C):
    return A*np.exp(-B*x)+C
p0=[1,1,1]
popt,pcov=curve_fit(model,x_data,y_data,p0=p0)
print("Fitted parameters (A,B,C):",popt)
print("True parameters (A,B,C):",(A_true,B_true,C_true))
