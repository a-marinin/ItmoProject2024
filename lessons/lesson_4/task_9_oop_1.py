'''
Задача 0
В файле task_9_oop_1.py:
1. Создайте класс Input, принимающий 1 аргумент при инициализации (Loc)
2. Создайте объект search (экземпляр класса Input)
3. Выведите в консоль значение аргумента Loc, объекта search
'''

# class Input:
#
#     def __init__(self, loc):
#         self.loc = loc
#
#
# search = Input('input#search')
#
# print(search.loc)


'''
Задача 1
1. Добавьте к классу Input атрибут объекта text
2. В этом же файле создайте:
- Класс Button
- Класс Title
- Класс Link
3. Для каждого класса пропишите артирубты text и loc
4. Создайте каждому из 4-х классов объекты, с любыми данными
5. Выведите в консоль text и loc каждого класса
'''



class Input:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text


class Button:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text


class Title:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text


class Link:

    def __init__(self, loc, text):
        self.loc = loc
        self.text = text


search = Input(loc='input#search', text='Поле поиска')
button = Button(loc='location#button', text='Текст кнопки')
title = Title(loc='test#test', text='Текст залоговка')
link = Link(loc='link#link', text='URL ссылки')

print(search.loc, search.text)
print(button.loc, button.text)
print(title.loc, title.loc)
print(link.loc, link.loc)
