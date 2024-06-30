import time
from lessons.lesson_12.pages.demoqa import DemoQa
from lessons.lesson_12.pages.alerts import Alerts
from lessons.lesson_12.pages.browser_tab import BrowserTab
from lessons.lesson_12.pages.accordion import AccordionPage
import pytest


@pytest.mark.parametrize("pages", [AccordionPage, Alerts, DemoQa, BrowserTab])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)  # Создаётся объект нашей некой страницы (реализовано с помощью переменной 'pages').
    page.visit()  # Посещаем страницу
    time.sleep(2)

    assert page.viewport.exist()  # Проверяем, что наш viewport существует
    assert page.viewport.get_dom_attribute('name') == 'viewport'  # Проверяем значение name у viewport
    assert page.viewport.get_dom_attribute('content') == 'width=device-width, initial-scale=1'  # Проверяем content
