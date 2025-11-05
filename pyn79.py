import re
text = input("Enter a string: ")
values = re.findall(r'"(.*?)"|\'(.*?)\'', text)
result = [v[0] if v[0] else v[1] for v in values]
print("Values between quotes:", result)
