def get_greatest_number(number1: int, number2: int) -> int:
    print('The following numbers are passed to the function: ', number1, ' and ', number2)
    greatest_number = max(number1, number2)
    smallest_number = min(number1, number2)
    print('The greates number is ', greatest_number, ' (because ', greatest_number, '>', smallest_number, ').')
    return greatest_number

# get_greatest_number(-9, 2) # Call the 1st task's function

def compare_2_numbers(number1: int, number2: int) -> None:
    # difference between the two numbers
    difference = max(number1, number2) - min(number1, number2)
    print('The difference between ', number1, ' and ', number2, ' is the following: ', difference)
    if difference == 135:
        print('Yes! The difference between these numbers equals 135.')
    if difference != 135:
        print('No. the difference between these numbers doesn\'t equals 135.')

compare_2_numbers(77, 99)  # Result: No
compare_2_numbers(-1, 134) # Result: Yez