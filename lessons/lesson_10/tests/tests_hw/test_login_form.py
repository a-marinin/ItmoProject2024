import time

from lessons.lesson_10.pages.form_page import FormPage


def test_login_form(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert not form_page.modal_dialog.exist()
    time.sleep(2)
    form_page.first_name.send_keys('tester')
    form_page.last_name.send_keys('testerovich')
    form_page.user_email.send_keys('test@ttt.tt')
    form_page.gender_radio_1.click_force()
    form_page.user_number.send_keys('9999999999')
    time.sleep(2)
    form_page.btn_submit.click_force()
    time.sleep(2)

    # Проверка на модальное окно (на наличие modal_dialog)
    assert form_page.modal_dialog.exist()
    form_page.btn_close_modal.click_force()  # Принудительно закрываем модальное окно
