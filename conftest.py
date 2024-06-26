import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    browser.set_window_size(width=1000, height=1000)  # Установили размер браузера.
    yield driver  # Чтобы наш драйвер мог использоваться в функции нужно написать слово 'yield'
    driver.quit()

