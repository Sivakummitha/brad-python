import pandas as pd
df=pd.read_csv("C:\\Users\\whynew.in\\OneDrive\\Desktop\\zomato.csv")
print(df.isnull().sum())
pivot = pd.pivot_table(
    df,
    index=['Country Code', 'City'],   
    values='Aggregate rating',        
    aggfunc='mean',                   
    fill_value=0
)
print("\nPivot Table with multiple indexes (Country Code & City):")
print(pivot)