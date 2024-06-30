from lessons.lesson_12.pages.alerts import Alerts
import time


def test_alert(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    assert not alert_page.alert()  # Проверяем, что есть активный алерт на странице

    alert_page.alertButton.click()
    time.sleep(2)
    assert alert_page.alert()  # Проверяем, что активных алертов на странице нет


def test_alert_text(browser):
    alert_page = Alerts(browser)

    alert_page.visit()
    alert_page.alertButton.click()
    assert alert_page.alert().text == 'You clicked a button'

    alert_page.alert().accepct()  # Принимаем аллерт
    assert not alert_page.alert()  # Проверяем, что активных алертов на странице нет


def test_confirm(browser):
    """ Отмена алерта """
    alert_page = Alerts(browser)

    alert_page.visit()
    alert_page.confirmButton.click()  # Кликаем на кнопку, вызывающую алерт
    time.sleep(2)
    alert_page.alert().dismiss()  # В окне алерта, отменяем алерт
    assert alert_page.confirmResult.get_text() == 'You selected Cancel'


def test_prompt(browser):
    """ Алерт Prompt """
    alert_page = Alerts(browser)
    name = 'Sasha'

    alert_page.visit()
    alert_page.promptButton.click()  # Кликаем на кнопку, вызывающую алерт
    time.sleep(2)
    alert_page.alert().send_keys(name)  # Передали текст в окно алерта Prompt
    alert_page.alert().accept()  # Нажали кнопку "ОК"
    assert alert_page.promptResult.get_text() == f'You entered { name }'
