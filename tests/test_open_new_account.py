import allure

from pages.open_new_account_page import OpenNewAccountPage


def test_open_new_account_page():
    new_account_page = OpenNewAccountPage()
    with allure.step("Открываем страницу создания нового аккаунта"):
        new_account_page.open_new_account_page()
    with allure.step("Выбираем тип счета"):
        new_account_page.select_account_type()
    with allure.step("Выбираем идентификатор первого существующего аккаунта "):
        new_account_page.select_the_first_existing_account()
    with allure.step("Нажимаем кнопку создания нового аккаунта"):
        new_account_page.click_open_new_account_button()