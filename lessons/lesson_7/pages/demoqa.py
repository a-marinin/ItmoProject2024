from selenium.common.exceptions import NoSuchElementException
from lessons.lesson_7.pages.base_page import BasePage


class DemoQa(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/'
        super().__init__(driver, self.base_url)

    def exist_icon(self):
        try:
            self.find_element(locator='#app > header > a')
        except NoSuchElementException:
            return False
        return True

    def click_on_the_icon(self):
        self.find_element(locator='#app > header > a').click()

    def click_on_the_btn(self):
        self.find_element(locator='#app > div > div > div.home-body > div > div:nth-child(1)').click()
