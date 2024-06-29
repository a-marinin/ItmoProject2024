import pytest
from selenium import webdriver

'''В данном случае декоратор @pytest.fixture изменяет поведение функции browser'''


@pytest.fixture(scope="session")  # Это декоратор (функция-обёртка, изменяющая поведение другой функции)
def browser():
    driver = webdriver.Chrome()  # Передали наш драйвер (создали объект драйвера).
    browser.set_window_size(width=1000, height=1000)  # Установили размер браузера.
    yield driver  # Чтобы наш драйвер мог использовать в функции (вызов/использование объекта драйвера).
    driver.quit()  # Закрываем драйвер.
