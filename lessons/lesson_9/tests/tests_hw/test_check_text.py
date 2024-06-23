from lessons.lesson_8.pages.demoqa import DemoQa
from lessons.lesson_8.pages.elements_page import ElementsPage


def test_check_footer_text(browser):
    # Проверка текста в футере на главной странице сайте demoqa.com
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()  # Переход на домашнюю страницу demoqa.com
    assert demo_qa_page.text_footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'  # Проверка текста


def test_check_element_text(browser):
    # Проверка текста по центру на странице demoqa.com/elements (Переход со страницы DemoQa)
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)

    demo_qa_page.visit()  # Переход на домашнюю страницу demoqa.com
    assert demo_qa_page.equal_url()  # Проверка URL на соответствие demoqa.com
    assert demo_qa_page.btn_elements.exist()  # Проверка того, что кнопка Elements существует
    demo_qa_page.btn_elements.click()  # Клик по кнопке Elements
    assert elements_page.equal_url()  # Проверка URL на соответствие demoqa.com/elements
    assert elements_page.text_center.get_text() == 'Please select an item from left to start practice.'


def test_page_elements(browser):
    # Проверка текста по центру на странице demoqa.com/elements (Перевод сразу на страницу Elements)
    el_page = ElementsPage(browser)
    el_page.visit()
    assert el_page.text_elements.get_text() == 'Please select an item from left to start practice.'  # Из задания №1

    assert el_page.icon.exist()  # Из задания №2
    assert el_page.btn_sidebar_first.exist()  # Из задания №2
    assert el_page.btn_sidebar_first_textbox.exist()  # Из задания №2
