#Change value of a key in a nested dictionary
company={1:{'a':1,'b':2},
         2:{'a':3,'b':3},
         3:{'a':3,'b':4}
         }
updated=company[3]['a']=5
print(updated)
print(company)