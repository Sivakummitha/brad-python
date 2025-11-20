def pilandrome(string):
    if string[::-1]:
        print(f"{string} is pilandrome")
    else:
        print(f"{string} is not a pilandrome")
pilandrome("madam")
