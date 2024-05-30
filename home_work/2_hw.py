def task_1():  # This is the 1st function
    var_int: int = 77
    var_float: float = 77.0
    var_str: str = 'This is a string variable'
    var_list: list = ["This", "is", "a", "list"]
    var_bool:bool = True

    print(var_int, var_float, var_str, var_list, var_bool) # Prints inside the function
    #return(var_int, var_float, var_str, var_list, var_bool) # Commit out to be able to print outside the function


task_1()  # Calls the 1st function
# print(task_1()) # Prints outside the 1st function (comment our the 9th row)


def task_2() -> None:  # This is the 3rd function
    a: list = [1, 2, 3, 5, 8, 13, 21]
    a_cut = a[:3]
    print(a[:3])  # Prints first 3 elements of the list
    print('Числа Фибоначчи - элементы числовой последовательности, где каждое последующее число равно сумме двух предыдущих чисел.')
    return a_cut


task_2()  # Calls the 2nd function


def task_3(a_number: int) -> int:  # This is the 3rd function
    square: int = a_number ** 2  # Square of the number
    print(a_number, ' в квадрате - это ', square)  # Prints inside the function
    return square


any_nuber: int = 77  # Задай любое число
print(task_3(any_nuber))  # Распечатай в консоль квадрат этого числа
