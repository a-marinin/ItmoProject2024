'''
Задача 3
В файле task_9_oop_3.py:
1. Создайте класс Sode (для определения типа газированной воды), принимающий 1 аргумент при инициализации
(отвечающий за добавку в выбираемому лимонаду).
2. В этом классе реализуйте метод show_my_drink(), выводящий на печать "Газировка и {ДОБАВКА}
в случае наличия добавка, а иначе отобразится следующая фраза: "Обычная газировка".
3. Для теста класса:
- Создайте 2 объект: один с добавкой, а другой - без неё.
- Вызовите мтеод show_my_drink() для каждого объекта.
'''


class Soda:

    def __init__(self, ing=None):
        self.ing = ing

    def show_my_drink(self):
        if self.ing:
            print(f'Газировка и {self.ing}')

        else:
            print('Обычная газировка')


drink1 = Soda()
drink2 = Soda('Малина')
drink1.show_my_drink()
drink2.show_my_drink()