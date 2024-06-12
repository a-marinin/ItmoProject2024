from lessons.lesson_7.pages.demoqa import DemoQa
import time


def check_icon(browser):
    demo_qa_page = DemoQa(browser)
    demo_qa_page.visit()
    demo_qa_page.icon.click()
    assert demo_qa_page.equal_url()
    assert demo_qa_page.exist_icon()
