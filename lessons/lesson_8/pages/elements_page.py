from lessons.lesson_8.pages.base_page import BasePage
from lessons.lesson_8.components.components import WebElement

"""
В файле elements_page.py создан класс ElementsPage - это страница элементов нашего сайта (demoqa.com/elements).
Класс ElementsPage наследуется от родительского класс BasePage. 
В классе ElementsPage описаны web-элементы (и их CSS-локаторы), находящиеся только на этой странице:
    1. text_center - Это текст, находящийся по центру страницы Элементов.
"""


class ElementsPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)

        self.text_center = WebElement(driver, '#app > div > div > div > div.col-12.mt-4.col-md-6')
        self.text_elements = WebElement(driver, 'dib.col-12:nth-child(2)')
