import pandas as pd
df=pd.read_csv("zomato.csv")
print(df.head(10).style.set_properties(**{'background-color': '#f8d7da', 
                                              'color': 'black', 
                                              'border': '1px solid gray'}))
print(df.tail(10).style.set_properties(**{'background-color': '#f8d7da', 
                                              'color': 'black', 
                                              'border': '1px solid gray'}))