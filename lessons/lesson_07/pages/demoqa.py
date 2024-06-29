from selenium.common.exceptions import NoSuchElementException
from lessons.lesson_07.pages.base_page import BasePage
from lessons.lesson_07.components.components import WebElement


class DemoQa(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

        self.icon = WebElement(driver, '#app > header > a')
        self.btn_elements = WebElement(driver, '#app > div > div > div.home-body > div > div:nth-child(1)')

    def exist(self):
        try:
            self.find_element()
        except NoSuchElementException:
            return False
        return True