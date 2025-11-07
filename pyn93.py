import pandas as pd
data = {
    'ID': [101, 102, 103, 104],
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 22, 28]
}
df = pd.DataFrame(data)
print("Default Index:")
print(df)
df_indexed = df.set_index('ID')
print("\nDataFrame after setting 'ID' column as index:")
print(df_indexed)
