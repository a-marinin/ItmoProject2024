'''
Задача - Создайте Базовый Класс
1. В каталоге pages создайте файл base_page.py
2. В Файле создайте класс BasePage.
3. При инициализации у класса есть 2 атрибута:
- driver - принимается в качестве аргумента
- base_url - не принимается, уставновлено значение по-умолчанию (https://demoqa.com/)
4. Создайте метод visit который возвращает переход на страницу (.get())
5. Создайте метод find_element:
- Метод принимает аргумент locator
- Метод возвращает поиск элемента (.find_elemnent())
6. Также необходимо добавить импорт  from selenium.webdriver.common.by import By
'''

from selenium.webdriver.common.by import By
import time
class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://demoqa.com/'

    def visit(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator):
        time.sleep(3)
        return self.driver.find_element(By.CSS_SELECTOR, locator)

    def get_url(self):
        return self.driver.current_url
