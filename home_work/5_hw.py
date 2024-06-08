# import requests
# from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

# Сначала попытался решить задачу с Requests + BS. Но не получилось. Решение с Selenium ниже.
# def find_login_elements_with_requests_and_bs() -> None:
#     # url = 'https://www.saucedemo.com/'
#     # r = requests.get(url).text
#     # print(r)  # Почему-то не находит нужные элементы (может быть потому что страница на JavaScript)
#
#     test_html = '<form><div class="form_group"><input class="input_error form_input" placeholder="Username" type="text" data-test="username" id="user-name" name="user-name" autocorrect="off" autocapitalize="none" value=""></div><div class="form_group"><input class="input_error form_input" placeholder="Password" type="password" data-test="password" id="password" name="password" autocorrect="off" autocapitalize="none" value=""></div><div class="error-message-container"></div><input type="submit" class="submit-button btn_action" data-test="login-button" id="login-button" name="login-button" value="Login"></form>'
#     soup = BeautifulSoup(test_html, 'html.parser')
#
#     field_username = soup.findAll('input')[0]  # Текстовое поле "username"
#     field_password = soup.findAll('input')[1]  # Текстовое поле "password"
#     submit_button = soup.find(id="login-button")  # Кнопка "submit"
#
#     if field_username and field_password and submit_button:
#         print('Все 3 элемента найдены:')
#         print('Это текстовое поле "username": ', type(field_username), field_username)
#         print('Это текстовое поле "password": ', type(field_password), field_password)
#         print('Это кнопка "submit": ', type(submit_button), submit_button)
#     else:
#         print('Один или несколько элементов не были найдены :(')


# find_login_elements_with_requests_and_bs()

def find_login_elements_with_selenium() -> None:
    driver = webdriver.Chrome()
    driver.get('https://www.saucedemo.com/')
    # print(driver.page_source)

    field_username = driver.find_element(By.CSS_SELECTOR, 'input.input_error[name="user-name"]')  # Текстовое поле "username"
    field_password = driver.find_element(By.CSS_SELECTOR, 'input.input_error[name="password"]')  # Текстовое поле "password"
    submit_button = driver.find_element(By.CSS_SELECTOR, 'input.submit-button')  # Кнопка "submit"
    # print(submit_button, field_username, field_password)

    if field_username and field_password and submit_button:
        print('Все 3 элемента найдены:')
        print('Это текстовое поле "username": ', type(field_username), field_username)
        print('Это текстовое поле "password": ', type(field_password), field_password)
        print('Это кнопка "submit": ', type(submit_button), submit_button)
    else:
        print('Один или несколько элементов не были найдены :(')

find_login_elements_with_selenium()