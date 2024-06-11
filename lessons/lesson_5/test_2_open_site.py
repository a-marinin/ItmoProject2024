'''
Задача: Написать свой вервый тест.
Тервый тест - это вход в Браузер
'''

from selenium import webdriver  # Импортируем webdriver из библиотеки selenium

driver = webdriver.Chrome()  # Создаём объект драйвера
driver.get('https://demoqa.com/')  # Вызываем метод get и ередаём в него URL-сайта
