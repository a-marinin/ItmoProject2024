from lessons.lesson_08.pages.elements_page import ElementsPage
import time


def test_visible_btn_sidebar_3rd_classwork(browser):  # Выполнили 3-е задание (deprecated)
    elements_page = ElementsPage(browser)  # Создание
    elements_page.visit()  # Посещение
    elements_page.btn_sidebar_first.find_element()  # Раскрываем меню сайдбара
    time.sleep(3)
    assert elements_page.btn_sidebar_first_textbox.exist()
    assert elements_page.btn_sidebar_first_textbox.visible()


def test_visible_btn_sidebar(browser):  # Выполнили 4-е задание
    elements_page = ElementsPage(browser)  # Создание
    elements_page.visit()  # Посещение
    assert elements_page.btn_sidebar_first_textbox.visible()  # Проверяем, что элемент виден


def test_not_visible_btn_sidebar(browser):
    elements_page = ElementsPage(browser)  # Создание
    elements_page.visit()  # Посещение
    assert elements_page.btn_sidebar_first_checkbox.visible()
    elements_page.btn_sidebar_first.click()
    time.sleep(2)
    assert not elements_page.btn_sidebar_first_checkbox.visible()  # Проверяем, что элемент НЕ виден
