'''
Задача: Написать свой вервый тест.
Тервый тест - это вход в Браузер
Второй тест - это поиск элемета на странице
'''

from selenium import webdriver  # Импортируем webdriver из библиотеки selenium
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()  # Создаём объект драйвера
driver.get('https://demoqa.com/')  # Вызываем метод get и ередаём в него URL-сайта

# Поиск элемента на странице
icon = driver.find_element(By.CSS_SELECTOR, 'header > a > img')
if icon is None:
    print('Элемент не найден')
else:
    print('Элекмент найден')
