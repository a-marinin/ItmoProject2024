from lessons.lesson_9.pages.demoqa import DemoQa
from lessons.lesson_9.pages.elements_page import ElementsPage

''' 1й тест-файл с текст кейсами из домашнего задания №9. '''


def test_navigation(browser):
    demo_qa_page = DemoQa(browser)  # Создали объект страницы DemoQa
    elements_page = ElementsPage(browser)  # Создали объект страницы ElementsPage

    demo_qa_page.visit()  # Посетили страницу DemoQa
    demo_qa_page.btn_elements.click()  # Нажали на кнопку "Elements"

    demo_qa_page.refresh()  # Обновили нашу страницу (DemoQa)
    browser.refresh()  # Обновили наш браузер
    browser.back()  # Перешли на шаг назад
    browser.forward()  # Перешли на шаг вперёд

    assert elements_page.equal_url()  # Проверяем страницу на соответствие URL
