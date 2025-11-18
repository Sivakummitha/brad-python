text=input("enter a text: ")
upper_case_count=0
lower_case_count=0
numbers_count=0
symbols_count=0
for ch in text:
    if ch.isupper():
        upper_case_count+=1
    elif ch.islower():
        lower_case_count+=1
    elif ch.isdigit():
        numbers_count+=1
    else:
        symbols_count+=1
print(f"uppercase letters are {upper_case_count}")
print(f"lowercase letters are {lower_case_count}")
print(f"numbes count are {numbers_count}")
print(f"symbols count are {symbols_count}")