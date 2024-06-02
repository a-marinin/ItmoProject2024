import calendar
from random import randint


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


# for month in range(12):
#     get_season_by_month_number(month)


def three_random_numbers(num1: int, num2: int, num3: int) -> None:
    print('The following numbers were generated: ', num1, ', ', num2, ' and ', num3)
    if num1 > 10 and num2 > 10 and num3 > 10:
        print('Yes. All of these numbers (', num1, num2, num3, ') are greater than 10.')
    else:
        print('No. Some of these numbers (', num1, num2, num3, ') are lower than 10.')


# three_random_numbers(randint(0, 99), randint(0, 99), randint(0, 99))


def find_positive_numbers(n1: int, n2: int, n3: int, n4: int, n5: int) -> None:
    print('The following numbers were generated: ', n1, n2, n3, n4, ' and ', n5)
    list_of_numbers = [n1, n2, n3, n4, n5]  # The list of all generated numbers
    list_of_positive_numbers = []  # An empty list to catch the positive numbers
    list_of_negative_numbers = []  # An empty list to catch the negative numbers
    list_of_zeros = []  # An empty list to catch Zeros (just in case

    for i in range(len(list_of_numbers)):
        if list_of_numbers[i] > 0:
            # print(list_of_numbers[i], ' is a positive number.')
            list_of_positive_numbers.append(list_of_numbers[i])  # Append all positive numbers
        elif list_of_numbers[i] == 0:
            # print(list_of_numbers[i], "It's a Zero!")
            list_of_zeros.append(list_of_numbers[i])  # Append zeros
        else:
            # print(list_of_numbers[i], ' is a negative number.')
            list_of_negative_numbers.append((list_of_numbers[i]))  # Append all negative numbers

    print('Statistic of your numbers:')
    print(len(list_of_positive_numbers), ' numbers were positive:', list_of_positive_numbers)
    print(len(list_of_negative_numbers), ' numbers were negative:', list_of_negative_numbers)
    print('And also you was lucky to catch', len(list_of_zeros), 'zeros', list_of_zeros)


#find_positive_numbers(randint(-99, 99), randint(-99, 99), randint(-99, 99), randint(-99, 99), 0)


def count_days(year: int, month: int) -> None:
    print('You entered', year, 'years and', month, 'months.')
    days_in_years = year * 12 * 29
    days_in_months = month * 29
    # print(days_in_years, days_in_months)
    total_days = days_in_years + days_in_months
    print("It's ", total_days, 'days ***')
    print('*** If we assume that there are 29 days in a month.')


count_days(2, 3)
