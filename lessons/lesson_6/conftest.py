import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser():
    driver = webdriver.Chrome()
    yield driver  # Чтобы наш драйвер мог использоваться в функции нужно написать слово 'yield'
    driver.quit()

