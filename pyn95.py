import pandas as pd
df1=pd.read_excel("C:\\Users\\whynew.in\\OneDrive\\Desktop\\Country-Code.xlsx")
df2=pd.read_csv("C:\\Users\\whynew.in\\OneDrive\\Desktop\\zomato.csv")
merging=pd.merge(df1,df2,axis=0)
print(merging)