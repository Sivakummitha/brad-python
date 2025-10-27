#Get the key of a minimum value from a dictionary
dict={'a': 1, 'b': 2, 'c': 3, 'd': 4}
minimum_dict=min(dict,key=dict.get)
print(minimum_dict)