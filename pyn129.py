import numpy as np
from scipy import stats
data=np.random.randn(1000)
print("First 10 random numbers:",data[:10])
print("Mean:",np.mean(data))
print("Median:",np.median(data))
print("Variance:",np.var(data))
print("Standard Deviation:",np.std(data))
mean,std=0,1
x=np.linspace(-3,3,10)
pdf=stats.norm.pdf(x,mean,std)
cdf=stats.norm.cdf(x,mean,std)
print("x values:",x)
print("PDF values:",pdf)
print("CDF values:",cdf)
