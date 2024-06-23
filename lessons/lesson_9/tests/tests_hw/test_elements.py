from lessons.lesson_9.pages.elements_page import ElementsPage


def test_find_elements(browser):
    elements_page = ElementsPage(browser)  # Создаём объект страницы ElementsPage
    elements_page.visit()  # Посещаем страницу Elements

    # Проверяем, что количество элементов с локатором - 9 штук.
    assert elements_page.btn_first_menu.check_count_elements(count=9)
