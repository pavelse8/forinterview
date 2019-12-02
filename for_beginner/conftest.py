import pytest
from selenium import webdriver


@pytest.fixture(scope="session")  # scope="session" означает что
# данная функция-фикстура будет исполнятся только 1 раз за тестовую сессию
def browser():
    driver = webdriver.Firefox()
    yield driver  # yield разделяет функцию на set_up и tear_down
    driver.quit()
