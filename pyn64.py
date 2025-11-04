import calendar
import datetime
print("Calendar using calendar module:\n")
y = datetime.datetime.now().year
m = datetime.datetime.now().month
print(calendar.month(y, m))
print("Calendar using datetime module and nested lists:\n")
first_day = datetime.date(y, m, 1)
start_day = first_day.weekday()
days_in_month = (datetime.date(y + (m // 12), (m % 12) + 1, 1) - first_day).days
weeks = []
week = []
for i in range(6):
    for j in range(7):
        day = i * 7 + j - start_day + 1
        if day < 1 or day > days_in_month:
            week.append("  ")
        else:
            week.append(f"{day:2}")
    weeks.append(week)
    week = []
print("Mo Tu We Th Fr Sa Su")
for w in weeks:
    print(" ".join(w))
