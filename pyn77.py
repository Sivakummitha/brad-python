import re
card = input("Enter your Debit Card number: ")
pattern = r'^[4-6][0-9]{15}$'
if re.fullmatch(pattern, card):
    print("Valid Debit Card Number")
else:
    print("Invalid Debit Card Number")
