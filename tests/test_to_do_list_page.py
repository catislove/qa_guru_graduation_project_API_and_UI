import allure
from allure_commons.types import Severity

from pages.to_do_list_page import ToDoListPage


to_do_list_page = ToDoListPage()


@allure.feature('Страница со списком задач')
@allure.story('Добавление задачи')
@allure.label('owner', 'Amalia')
@allure.tag('web')
@allure.severity(Severity.NORMAL)
def test_add_new_todo():
    with allure.step("Открываем страницу со списком задач"):
        to_do_list_page.open_to_do_list_page()
    with allure.step("Добавляем задачу и проверяем, что она появилась в списке"):
        to_do_list_page.add_and_check_new_todo("TestTODO")

@allure.feature('Страница со списком задач')
@allure.story('Вычеркивание задачи')
@allure.label('owner', 'Amalia')
@allure.tag('web')
@allure.severity(Severity.NORMAL)
def test_completed_todo():
    with allure.step("Открываем страницу со списком задач"):
        to_do_list_page.open_to_do_list_page()
    with allure.step("Вычеркиваем задачу и проверяем, что она вычеркнулась"):
        to_do_list_page.completed_todo(" Practice magic")