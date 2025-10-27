dict = {"name": "Siva", "age": 21, "marks": 90}
print("Original Dictionary:",dict)

print(" get():", dict.get("name"))
print(" keys():", dict.keys())
print(" values():", dict.values())
print(" items():", dict.items())

dict.update({"marks": 95, "city": "Hyderabad"})
print(" update():", dict)

removed_value = dict.pop("age")
print("pop(): removed 'age' ->", removed_value)
print("After pop():", dict)

last_item =dict.popitem()
print(" popitem(): removed last item ->", last_item)
print(" After popitem():", dict)

dict.setdefault("country", "India")
print(" setdefault():", dict)

new_dict = dict.copy()
print(" copy():", new_dict)

dict.clear()
print(" clear():",dict)