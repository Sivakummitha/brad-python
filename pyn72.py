import re
def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return "Valid Email ID"
    else:
        return "Invalid Email ID"
email = input("Enter your email ID: ")
print(validate_email(email))
