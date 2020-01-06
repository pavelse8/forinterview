import pytest
from pages.login_page import LoginPage

LINK_LOGIN_PAGE = "https://mail.ru/"


@pytest.mark.mail
def test_authorize_for_rop(browser):
    login_page = LoginPage(browser, LINK_LOGIN_PAGE)
    login_page.open_page()
    login_page.enter_the_login()
    login_page.enter_the_password()
    mailbox_page = login_page.go_to_mailbox_page()
    mailbox_page.create_new_letter()
    mailbox_page.fill_adress()
    mailbox_page.fill_body()
    mailbox_page.send_letter()
