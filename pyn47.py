#Write a Python class which has two methods get_String and print_String. get_String accept a string from the user and print_String print the string in upper case
class StringManipulator:
    def __init__(self):
        self.user_string = ""
    def get_String(self):
        self.user_string = input("Enter a string: ")
    def print_String(self):
        print(self.user_string.upper())
if __name__ == "__main__":
    string_obj = StringManipulator()
    string_obj.get_String()
    string_obj.print_String()