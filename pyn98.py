import pandas as pd
df=pd.DataFrame({'name':['siva','balu','charan','dhanush','eshwar','fanendra'],'age':[20,30,23,45,56,24,]})
print(df)
df1=df.iloc[:3]
df2=df.iloc[3:]
print(df1)
print(df2)
print(df)