from lessons.lesson_12.pages.base_page import BasePage
from lessons.lesson_12.components.components import WebElement


class BrowserTab(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/browser-windows'
        super().__init__(driver, self.base_url)

        self.new_tab = WebElement(driver, '#tabButton')
