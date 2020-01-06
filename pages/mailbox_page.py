from .base_page import BasePage
from .worksheet_list_page import WorkSheetPage
from selenium.webdriver.common.by import By
import time

CORRECT_LINK_CRP = 'http://ecm4-test.slms.ru/crp_news/list/'


class NewsPage(BasePage):
    def title_correct_crp(self):
        if self.browser.current_url == CORRECT_LINK_CRP:
            return True
        else:
            return False

    def return_worklist_page(self):
        url_wl = WorkSheetPage.CORRECT_LINK_CRP
        return WorkSheetPage(browser=self.browser, url=url_wl)


