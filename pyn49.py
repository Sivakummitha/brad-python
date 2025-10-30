#Write a Python class Square, and define two methods that return the square area and perimeter.
class Square:
    def __init__(self, side):
        self.side = side
    def get_area(self):
        return self.side * self.side
    def get_perimeter(self):
        return 4 * self.side
if __name__ == "__main__":
    my_square = Square(5) 
    area = my_square.get_area()
    perimeter = my_square.get_perimeter()
    print(f"The area of the square is: {area}")
    print(f"The perimeter of the square is: {perimeter}")
