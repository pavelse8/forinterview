from .base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

NEW_LETTER_BUTTON = (By.XPATH, '//span[@title="Написать письмо"]')
SEND_LETTER_BUTTON = (By.XPATH, '//span[@class="button2__txt"][text()="Отправить"]')
BODY_LETTER = (By.XPATH, '//div[@role="textbox"]/div/div')
ADRESS = (By.XPATH, "(//input[@class='container--H9L5q size_s_compressed--2c-eV'])[1]")


class MailboxPage(BasePage):

    def create_new_letter(self):
        self.to_element_click(self.browser.find_element(NEW_LETTER_BUTTON[0], NEW_LETTER_BUTTON[1]))

    def fill_body(self):
        body = self.browser.find_element(BODY_LETTER[0], BODY_LETTER[1])
        body.send_keys("ТЕКСТ ПИСЬМА")

    def fill_adress(self):
        adress = self.browser.find_element(ADRESS[0], ADRESS[1])
        adress.send_keys("adresstheletter@mail.ru")

    def send_letter(self):
        self.to_element_click(self.browser.find_element(SEND_LETTER_BUTTON[0], SEND_LETTER_BUTTON[1]))
