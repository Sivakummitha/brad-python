#program to print unique values in a list
list = [1, 2, 2, 3, 4, 4, 5, 1]
uniquevalues = []
for item in list:
    if item not in uniquevalues:
        uniquevalues.append(item)
print(uniquevalues)