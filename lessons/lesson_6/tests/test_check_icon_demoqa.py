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


from selenium.webdriver.common.by import By


def check_icon(browser):
    browser.get('https://demoqa.com/')  # Вызываем метод get и ередаём в него URL-сайта

    # Поиск элемента на странице
    icon = browser.find_element(By.CSS_SELECTOR, 'header > a > img')
    if icon is None:
        print('Элемент не найден')
    else:
        print('Элекмент найден')
        