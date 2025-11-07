import pandas as pd
import re
data = pd.Series([123, 45, 6789, 5, 98765])
def add_leading_zeros(x):
    return re.sub(r'^', '0' * (8 - len(str(x))), str(x))
result = data.apply(add_leading_zeros)
print("Original Series:")
print(data)
print("\nSeries after adding leading zeros:")
print(result)
