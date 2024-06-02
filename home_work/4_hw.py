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

class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.addition = Math.addition(self, a, b)
        self.multiplication = Math.multiplication(self, a, b)
        self.division = Math.division(self, a, b)
        self.subtraction = Math.subtraction(self, a, b)

    def addition(self, a, b):
        addition = a + b
        return "The addition of 2 numbers ({} and {}) is equal to {}".format(a, b, addition)

    def multiplication(self, a, b):
        multiplication = a * b
        return "The multiplication of 2 numbers ({} and {}) is equal to {}".format(a, b, multiplication)

    def division(self, a, b):
        division = a / b
        return "The division of 2 numbers ({} and {}) is equal to {}".format(a, b, division)

    def subtraction(self, a, b):
        subtraction = a - b
        return "The subtraction of 2 numbers ({} and {}) is equal to {}".format(a, b, subtraction)


test = Math(25, 5)
print(test.addition)
print(test.multiplication)
print(test.division)
print(test.subtraction)