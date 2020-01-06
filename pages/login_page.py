from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .mailbox_page import MailboxPage
import time

LOGIN_PAGE_URL = "https://mail.ru/"
LOGIN_FIELD = (By.XPATH, "//input[@id='mailbox:login']")
PASSWORD_FIELD = (By.XPATH, "//input[@id='mailbox:password']")
AUTHORIZE_BUTTON = (By.XPATH, "//input[@class='o-control']")

# USER (USERNAME, PASSWORD)
USER = ('inboxfortesting', 'mailpassword123')


class LoginPage(BasePage):

    def enter_the_login(self):
        loginfield = self.browser.find_element(LOGIN_FIELD[0], LOGIN_FIELD[1])
        loginfield.send_keys(USER[0])
        self.to_element_click(self.browser.find_element(AUTHORIZE_BUTTON[0], AUTHORIZE_BUTTON[1]))

    def enter_the_password(self):
        passwordfield = self.browser.find_element(PASSWORD_FIELD[0], PASSWORD_FIELD[1])
        passwordfield.send_keys(USER[1])

    def go_to_mailbox_page(self):
        self.to_element_click(self.browser.find_element(AUTHORIZE_BUTTON[0], AUTHORIZE_BUTTON[1]))
        time.sleep(4)
        return MailboxPage(browser=self.browser, url=self.browser.current_url)
