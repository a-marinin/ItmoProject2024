import time
from lessons.lesson_12.pages.demoqa import DemoQa
from lessons.lesson_12.pages.alerts import Alerts
from lessons.lesson_12.pages.browser_tab import BrowserTab
from lessons.lesson_12.pages.accordion import AccordionPage
import pytest


def test_check_title_demo(browser):
    demo_qa_page = DemoQa(browser)  # Создаём новый объект DemoQa

    demo_qa_page.visit()  # Посещаем страницу demoqa.com
    assert browser.title == 'DEMOQA'  # Сравниваем Title у browser с эталонным.


@pytest.mark.parametrize("pages", [AccordionPage, Alerts, DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    """
    Как работает декоратор:
    Наша переменная 'pages' помогает нам создавать объект нашей страницы.
    Вместо переменной 'pages' у нас будет подставляться каждая страница из списка, каждый класс.
    И работать этот цикличный список будет столько раз, сколько у нас есть аргументов (3 в нашем случае).
    """
    page = pages(browser)  # Создаётся объект нашей некой страницы (реализовано с помощью переменной 'pages').
    page.visit()  # Посещаем страницу
    time.sleep(2)  # Ждём
    assert page.get_title() == 'DEMOQA'  # Проверили title у текущей страницы (из цикла)
