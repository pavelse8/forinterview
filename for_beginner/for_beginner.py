# Запустить, чтобы проверить, что драйвер работает
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("http://www.python.org")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

# Page Object определяет в себе части:
#
#
# Base Page \ Base Class — Реализует в себе необходимые методы для работы с webdriver.
# Page Object \ Page Class — Реализует методы для работы с элементами на веб-страницах.
# Tests — Реализует тесты, описанные бизнес-логикой тест-кейса.
#
#
# Для начала необходимо реализовать инициализацию для WebDriver. Описывать её будем в фикстуре. Фикстуры в pytest —
# функции которые имеют свою периодичность выполнения. Это альтернативная замена SetUp и TearDown методов в unittest.
# С помощью фикстуры, можно подготовить начальное состояние системы для проведения тестирования.
#
#
# В pytest есть зарезервированное имя для файла с фикстурами — conftest.py.
