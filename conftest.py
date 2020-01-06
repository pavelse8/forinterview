import pytest
from selenium import webdriver

EXECT_PATH = "drivers_for_windows/chrome 79/chromedriver.exe"


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome(executable_path=EXECT_PATH)
    yield browser
    browser.quit()
