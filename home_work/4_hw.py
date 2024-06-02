class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.square = Rectangle.square(self, width, height)
        self.perimeter = Rectangle.perimeter(self, width, height)

    def square(self, width, height):
        square = width * height
        # return square
        return "The square of the rectangle ({}x{}) is {}.".format(width, height, square)

    def perimeter(self, width, height):
        perimeter = (width + height) * 2
        # return perimeter
        return "The perimetr of the rectangle ({}x{}) is {}.".format(width, height, perimeter)


rectangle_1 = Rectangle(2, 3)
rectangle_2 = Rectangle(5, 9)
rectangle_3 = Rectangle(77, 99)

print('1st rectangle ----> ', rectangle_1.square, rectangle_1.perimeter)
print('2nd rectangle ----> ', rectangle_2.square, rectangle_2.perimeter)
print('3rd rectangle ----> ', rectangle_3.square, rectangle_3.perimeter)
