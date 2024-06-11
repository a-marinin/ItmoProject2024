'''
Задание 1:
1. В директории tests создайте файл test_check_icon_demoqa.py
2. Напишите тест:
- Зайти на страницу https://demoqa.com/
- Найти элемент "#app > header > a"
3. Запустить через pytest
'''

# from selenium import webdriver  # Импортируем webdriver из библиотеки selenium
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()  # Создаём объект драйвера
# driver.get('https://demoqa.com/')  # Вызываем метод get и ередаём в него URL-сайта
#
# # Поиск элемента на странице
# icon = driver.find_element(By.CSS_SELECTOR, 'header > a > img')
# if icon is None:
#     print('Элемент не найден')
# else:
#     print('Элекмент найден')

'''
Задание 2
1. Откройте наш тест
2. Добавьте фикстуру browser как аргумент функции теста
3. Сотрите строку driver = webdriver.Chrome()
4. Сотрите строку from selenium import webdriver
5. Запустить через pytest
'''


# from selenium.webdriver.common.by import By
from lessons.lesson_6.pages.demoqa import DemoQa
import time

# def check_icon(browser):
    # browser.get('https://demoqa.com/')  # Вызываем метод get и ередаём в него URL-сайта
    #
    # # Поиск элемента на странице
    # icon = browser.find_element(By.CSS_SELECTOR, 'header > a > img')
    # if icon is None:
    #     print('Элемент не найден')
    # else:
    #     print('Элекмент найден')

'''
    Задача - Изменить код текста, чтобы он работал с нашими классами.
    1. Уберите импорт
    2. Вместо селениума испортируйте класс DemoQa из pages.demoqa
    3. Закомментируйте весь код внутри функции exist_icon
'''

# def check_icon(browser):
    # demo_qa_page = DemoQa(browser)
    # demo_qa_page.visit()
    # assert demo_qa_page.exist_icon()

'''
Задача - Изменить тест кейс
1. Зайти на сайт https://demoqa.com/
2. Кликнуть на страницу https://demoqa.com/
3. Найти элемент "#app > header > a"

Для этого мы делаем следующее:
1. В файле demoqa.py, в классе DemoQa добавим метод click_on_the_icon
- Метод возвращает клик по элементу. Для этого найдите элемент и добавьте .click()
2. В файле test_check_icon_demoqa.py добавьте вызов метода, в соответствии с тест кейсом
3. Запустите программу

Чтобы понять, что происходит:
1. В файле базового класса добавьте импорт time
2. В методе find_element первой строкой добавьте time.sleep(3)
3. Запустите программу
'''

def check_icon(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    time.sleep(3)
    demo_qa_page.click_on_the_icon()
    time.sleep(3)
    assert demo_qa_page.equal_url()
    assert demo_qa_page.exist_icon()

'''
Задача - Добавить проверку на URL после клика
1. Зайти на страинцу https://demoqa.com/
2. Кликнуть по элементу "app > header > a"
3. Проверить URL на соответствие https://demoqa.com/
4. Найти элемент "#app > header > a"

Для этого мы:
1. В базовый класс добавляем метод get_url
- Метод get_url должен возвращать текущий URL.
2. В класс страницы добавляем метод equal_url:
- Метод equal_url должен вызывать get_url и сравнивать его со строкой 'https://demoqa.com/'
- Метод equal_url должен возвращать True если проверка пройдена и False - если не пройденна
3. В тесте, в соответствии с кейсом, добавим проверку assert, которая вызывает equal_url()
'''

