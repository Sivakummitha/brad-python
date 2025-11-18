string=str(input("enter a string:"))
for ch in string:
    if string.count(ch)==1:
        print("first non repeating characters",ch)
        break
    else:
        print("no non repeating characters found")