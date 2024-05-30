def get_greatest_number(number1: int, number2: int) -> int:
    print('The following numbers are passed to the function: ', number1, ' and ', number2)
    greatest_number = max(number1, number2)
    smallest_number = min(number1, number2)
    print('The greates number is ', greatest_number, ' (because ', greatest_number, '>', smallest_number, ').')
    return greatest_number


get_greatest_number(-9, 2)
