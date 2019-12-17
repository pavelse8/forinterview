from pages.login_page import LoginPage
from pages.news_page import NewsPage
import pytest
import allure
from allure_commons.types import AttachmentType

LINK_LOGIN_PAGE = "http://ecm4-test.slms.ru/login/"
ROP = ('alexanderalexandrov', 'alexanderalexandrov1')


@allure.feature('Тестирование авторизации')
@allure.story('Тест создания рабочего листа (ПОЛОЖИТЕЛЬНЫЙ)')
@allure.severity('blocker')
@pytest.mark.login
def test_authorize_for_rop(browser):
    login_page = LoginPage(browser, LINK_LOGIN_PAGE)
    with allure.step('Открываем страницу'):
        login_page.open()
    with allure.step('Вводим данные Ропа для авторизации'):
        login_page.enter_the_login_and_password_rop()
    with allure.step('Авторизуемся и переходим на страницу новостей'):
        newspage = login_page.go_to_news_page()
    with allure.step('Переходим на страницу списка рабочих листов'):
        worksheetlist = newspage.return_worklist_page()
        worksheetlist.open()
    worksheetlist
