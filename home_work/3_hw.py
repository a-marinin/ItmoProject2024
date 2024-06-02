import calendar

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

# compare_2_numbers(77, 99)  # Result: No
# compare_2_numbers(-1, 134) # Result: Yes


def get_season_by_month_number(month_number: int) -> None:

    month_number_list = list(range(1, 13))  # The list of numeric months (1-12)
    month_name_list = list(calendar.month_name[1:])  # The list of string months (Jan-Dec)
    season_list = ('Winter ' * 2 + 'Spring ' * 3 + 'Summer ' * 3 + 'Autumn ' * 3 + 'Winter').split()  # The list of seasons (stirng)
    result_list = [list(x) for x in zip(month_number_list, month_name_list, season_list)]  # The result list

    print('You entered the following number: ', result_list[month_number-1][0])
    print('It equals to the following month: ', result_list[month_number-1][1])
    print('And this month is located is the following season: ', result_list[month_number-1][2])
    print()


for month in range(12):
    get_season_by_month_number(month)
