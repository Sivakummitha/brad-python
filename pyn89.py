try:
    num = int("abc")
except ValueError as e:
    print("Caught ValueError Exception:", e)
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Caught ZeroDivisionError Exception:", e)