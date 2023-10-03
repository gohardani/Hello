class Rectangle:
    """
    Area and Perimeter of Rectangle
    >>> "Enter length of rectangle:"
    length
    >>> "Enter width of rectangle:"
    width
    >>> p1 = Rectangle(length, width)
    >>> p1. calculate_area()
    >>> p1.calculare_perimeter()
    """

    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def calculate_area(self):
        area = self.length * self.width
        print("Area of Rectangle is equal to:", area)

    def calculare_perimeter(self):
        perimeter = 2 * (self.length + self.width)
        print("Perimeter of Rectangle is equal to:", perimeter)


length = int(input("Enter length of rectangle:"))
width = int(input("Enter width of rectangle:"))
p1 = Rectangle(length, width)
print(15 * "*", 'Result', 15*'*')
p1. calculate_area()
print(15 * "*", 'Result', 15*'*')
p1.calculare_perimeter()
print(40 * "*")

#print(Rectangle.__doc__)

