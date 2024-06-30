from lessons.lesson_12.pages.browser_tab import BrowserTab
import time


def test_browser_tab(browser):
    page_browser = BrowserTab(browser)
    page_browser.visit()

    assert len(browser.window_handles) == 1  # Проверяем, что открыта 1 вкладка
    page_browser.new_tab.click()  # Открываем новое окно
    time.sleep(2)
    assert len(browser.window_handles) == 2  # Проверяем, что открыты 2 вкладки

    browser.switch_to.window(browser.window_handles[0])  # Переключаемся на 1-ю вкладку
    time.sleep(2)
