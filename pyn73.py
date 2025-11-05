import re
def validate_phone_number(number):
    pattern = r'^\+?\d{1,3}?[-.\s]?\d{10}$'
    if re.match(pattern, number):
        return "Valid Telephone Number"
    else:
        return "Invalid Telephone Number"
number = input("Enter Telephone Number: ")
print(validate_phone_number(number))
