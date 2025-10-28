#write a program to Remove Reduntant Substrings from Strings List
string_list=["apple","banana","apple","onion","watermelon","onion"]
unique=[]
for i in string_list:
    if i not in unique:
        unique.append(i)
print(unique)
