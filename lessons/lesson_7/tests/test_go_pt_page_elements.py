from lessons.lesson_7.pages.demoqa import DemoQa
from lessons.lesson_7.pages.elements_page import ElementsPage

def test_go_to_page_elements(browser):
    demo_qa_page = DemoQa(browser)
    elements_page = ElementsPage(browser)

    demo_qa_page.visit()
    assert demo_qa_page.equal_url()
    demo_qa_page.click_on_the_btn()
    assert elements_page.equal_url()