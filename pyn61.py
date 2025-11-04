from datetime import date
d = date(1996, 12, 11)
print(d)
#
from datetime import date
t = date.today()
print(t)
#
from datetime import date
t = date.today()
print(t.year)
print(t.month)
print(t.day)
#
from datetime import date
t = date.today()
print(t.year)
print(t.month)
print(t.day)
#
from datetime import date
t = date.today()
date_str = t.isoformat()
print(date_str)
print(type(date_str))
