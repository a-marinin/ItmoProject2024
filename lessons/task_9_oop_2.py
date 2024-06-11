'''
Задача 2
В файле task_9_oop_2.py:
1. Создайте класс Page, принимающий 1 аргумент при инициализации url
2. В этом классе реализуйте метод get() который выводит на печать url
3. Создайте объект home и вызовите мтеод get()
'''

class Page:

    def __init__(self, url):
        self.url = url

    def get(self):
        print(self.url)


home = Page('https://demoqa.com/')
home.get()
