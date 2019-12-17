from pages.login_page import LoginPage
from pages.news_page import NewsPage
import pytest
import allure
from allure_commons.types import AttachmentType

LINK_LOGIN_PAGE = "http://ecm4-test.slms.ru/login/"
ROP = ('alexanderalexandrov', 'alexanderalexandrov1')


@allure.feature('Тестирование авторизации')
@allure.story('Тест отоброжение полей и кнопки для авторизации')
@allure.severity('normal')
@pytest.mark.login
def test_should_be_login_button_on_login_page(browser):

    login_page = LoginPage(browser, LINK_LOGIN_PAGE)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    with allure.step('Открываем страницу'):
        login_page.open()  # открываем страницу
    with allure.step('Вводим данные Ропа для авторизации'):
        login_page.enter_the_login_and_password_rop()
    with allure.step('Делаем скриншот'):  # Шаг теста для отчета allure
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    with allure.step('Проверяем существование кнопки авторизации'):
        login_page.should_be_login_button()          # выполняем метод страницы - переходим на страницу логина


@allure.feature('Тестирование авторизации')
@allure.story('Тест авторизации с корректным логином (ПОЛОЖИТЕЛЬНЫЙ)')
@allure.severity('normal')
@pytest.mark.login
def test_authorize_for_rop(browser):
    login_page = LoginPage(browser, LINK_LOGIN_PAGE)
    with allure.step('Открываем страницу'):
        login_page.open()
    with allure.step('Вводим данные Ропа для авторизации'):
        login_page.enter_the_login_and_password_rop()
    with allure.step('Нажимаем кнопку авторизации'):
        newspage = login_page.go_to_news_page()
    with allure.step('Делаем скриншот'):  # Шаг теста для отчета allure
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    with allure.step('Проверяем что загрузилась страница новосте'):
        assert newspage.title_correct_crp()


@allure.feature('Тестирование авторизации')
@allure.story('Тест авторизации с некорректным логином (ОТРИЦАТЕЛЬНЫЙ)')
@allure.severity('normal')
@pytest.mark.login
def test_authorize_for_wrong_user(browser):
    login_page = LoginPage(browser, LINK_LOGIN_PAGE)
    with allure.step('Открываем страницу'):
        login_page.open()
    with allure.step('Вводим данные Ропа для авторизации'):
        login_page.enter_the_wrong_login_and_password_rop()
    with allure.step('Нажимаем кнопку авторизации'):
        newspage = login_page.go_to_news_page()
    with allure.step('Делаем скриншот'):  # Шаг теста для отчета allure
        allure.attach(browser.get_screenshot_as_png(), name='Screenshot', attachment_type=AttachmentType.PNG)
    with allure.step('Проверяем что загрузилась страница новосте'):
        assert not newspage.title_correct_crp()
