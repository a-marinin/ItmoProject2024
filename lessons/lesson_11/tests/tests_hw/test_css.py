from lessons.lesson_11.pages.text_box import TextBox


def text_text_box_submit(browser):
    text_box = TextBox(browser)

    text_box.visit()

    assert text_box.submit.check_css('color', 'rgba(255, 255, 255, 1)')

    # Когда проверяем RGBA - указываются 4 значения.
    assert text_box.submit.check_css('backgroundColor', 'rgba(0, 123, 255, 1)')
    # Когда проверяем RGB - указываются 3 значения.
    assert text_box.submit.check_css('borderColor', 'rgb(0, 123, 255)')
