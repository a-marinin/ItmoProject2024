'''
Задача - Создайте Класс страницы
1. В каталоге pages создайте файл demoqa.py
2. В файле создайте класс DemoQa:
- Класс DemoQA пока не имеет атрибутов, конструктор не требуется
3. Наследуйте класс DemoQa от класса BasePage
(при импорте не забудьте указать путь вместе с каталогом pages.base_page)
4. Создайте метод exit_icon:
- Метод вызывает метод find_element родительского класса и передаёт в него локатор locator='#app > header > a'
5. Для красоты кода воспользуйтесь конструкцией try except
6. Исключения надо импортировать 'NoSuchElementException'
'''

from selenium.common.exceptions import NoSuchElementException
from lessons.lesson_6.pages.base_page import BasePage

class DemoQa(BasePage):

    def exist_icon(self):
        try:
            self.find_element(locator='#app > header > a')
        except NoSuchElementException:
            return False
        return True

    def click_on_the_icon(self):
        self.find_element(locator='#app > header > a').click()

    def equal_url(self):
        if self.get_url() == 'https://demoqa.com/':
            return True
        else:
            return False
