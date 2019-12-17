from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from .news_page import NewsPage
import time

LOGIN_FIELD = (By.XPATH, "//input[@name='username']")
PASSWORD_FIELD = (By.XPATH, "//input[@name='password']")
LOGIN_BUTTON = (By.XPATH, "//button[@name='login']")

# DEALERSHIP (USERNAME, PASSWORD)
ROP = ('alexanderalexandrov', 'alexanderalexandrov1')
LOGISTICIAN = ('alexanderalexandrov', 'alexanderalexandrov')
WARRANTY_ENGINEER = ('singener', 'singener1')

# IMPORTER (USERNAME, PASSWORD)
CHIEF = ('uldasheva', 'uldasheva1')
USED_CAR_MANAGER = ('eromanov', 'eromanov1')
DISTRIBUTOR_LOGISTICIAN = ('tisaeva2', 'tisaeva21')
DISTRIBUTOR_WARRANTY_ENGINEER = ('lazarev', 'lazarev')

# WRONG (USERNAME, PASSWORD)
WRONGUSER = ('dsfsdf123123123', 'alexanderalexandrov1')

class LoginPage(BasePage):

    def should_be_login_button(self):
        time.sleep(3)
        assert self.is_element_present(LOGIN_BUTTON)

    def enter_the_login_and_password_rop(self):
        loginfield = self.browser.find_element(LOGIN_FIELD[0], LOGIN_FIELD[1])
        loginfield.send_keys(ROP[0])
        passwordfield = self.browser.find_element(PASSWORD_FIELD[0], PASSWORD_FIELD[1])
        passwordfield.send_keys(ROP[1])

    def enter_the_wrong_login_and_password_rop(self):
        loginfield = self.browser.find_element(LOGIN_FIELD[0], LOGIN_FIELD[1])
        loginfield.send_keys(WRONGUSER[0])
        passwordfield = self.browser.find_element(PASSWORD_FIELD[0], PASSWORD_FIELD[1])
        passwordfield.send_keys(WRONGUSER[1])

    def go_to_news_page(self):
        login_button = self.browser.find_element(LOGIN_BUTTON[0], LOGIN_BUTTON[1])
        self.to_element_click(login_button)
        time.sleep(3)
        return NewsPage(browser=self.browser, url=self.browser.current_url)
