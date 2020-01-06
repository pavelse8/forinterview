class BasePage():
    def __init__(self, browser, url,
                 timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open_page(self):
        self.browser.get(self.url)

    def to_element_click(self, element):
        self.browser.execute_script("arguments[0].click();", element)

