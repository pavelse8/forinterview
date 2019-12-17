class BasePage():
    def __init__(self, browser, url,
                 timeout=10):  # init это метод конструктор, вызывается, когда инициализируется новый объект класса
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def to_element_click(self, element):
        self.browser.execute_script("arguments[0].click();", element)

    def is_element_present(self, selenium_turple):
        try:
            self.browser.find_element(selenium_turple[0], selenium_turple[1])
        except:
            return False
        return True
