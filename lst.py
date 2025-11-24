"""list=[1,2,2,3,4,5,6,3]
unique=[]
for i in list:
    if i not in unique:
        print(unique.append(i))

print("uniques values is : ",unique)"""

list=[1,2,2,3,4,5,6,3]
unique_vales=set(list)
count_uniq=len(unique_vales)
print(f'count of uniques valies is {count_uniq}')