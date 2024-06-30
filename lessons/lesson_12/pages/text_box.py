from lessons.lesson_11.pages.base_page import BasePage
from lessons.lesson_11.components.components import WebElement


class TextBox(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.name = WebElement(driver, '#userName')
        self.submit = WebElement(driver, '#submit')