date = input("Enter date in yyyy-mm-dd format: ")
parts = date.split("-")
new_date = parts[2] + "-" + parts[1] + "-" + parts[0]
print("Date in dd-mm-yyyy format:", new_date)
