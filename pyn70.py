from datetime import date
d=int(input("Enter birth day: "))
m=int(input("Enter birth month: "))
y=int(input("Enter birth year: "))
dob = date(y, m, d)
today = date.today()
years = today.year - dob.year
months = today.month - dob.month
days = today.day - dob.day
if days < 0:
    months -= 1
    days += (date(today.year, today.month, 1) - date(today.year, today.month - 1, 1)).days
if months < 0:
    years -= 1
    months += 12
print("Age:", years, "years", months, "months", days, "days")
