import time
from lessons.lesson_10.pages.text_box import TextBox


def test_placeholder(browser):
    """ Проверка значения атрибута элемента """
    text_box_page = TextBox(browser)

    text_box_page.visit()
    assert text_box_page.name.get_dom_attribute('placeholder') == 'Full Name'
