from lessons.lesson_9.pages.demoqa import DemoQa


def test_check_title_demo(browser):
    demo_qa_page = DemoQa(browser)  # Создаём новый объект DemoQa

    demo_qa_page.visit()  # Посещаем страницу demoqa.com
    assert browser.title == 'DEMOQA'  # Сравниваем Title у browser с эталонным.
