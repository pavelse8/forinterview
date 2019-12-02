import allure
from allure_commons.types import Severity
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver

@allure.title('Результатов поиска больше 10')
@allure.severity(Severity.BLOCKER)
def test_yandex_search():
    driver = webdriver.Firefox()
    with allure.step('Открываем страницу поиска'):
        driver.get('https://ya.ru')

    with allure.step('Ищем market.yandex.ru'):
        search_input = driver.find_element_by_xpath('//input[@id="text"]')
        search_button = driver.find_element_by_xpath('//div[@class="search2__button"]//button[@type="submit"]')
        search_input.send_keys('market.yandex.ru')
        search_button.click()

    def check_results_count(driver):
        inner_search_results = driver.find_elements_by_xpath('//li[@class="serp-item"]')
        return len(inner_search_results) >= 10

    with allure.step('Ожидаем что колличество результатов теста будет больше 10'):
        WebDriverWait(driver, 5, 0.5).until(check_results_count, 'Количество результатов поиска меньше 10')

    with allure.step('Переходим по ссылке первого результата'):
        search_results = driver.find_elements_by_xpath('//li[@class="serp-item"]')
        link = search_results[0].find_element_by_xpath('.//h2/a')
        link.click()

    with allure.step('Проверяем корректность Title страницы'):
        assert driver.title == 'Яндекс.Маркет — выбор и покупка товаров из проверенных интернет-магазинов'
# запускать так
#test test_yandex_search.py --alluredir=allure_results  положит в папку allure_results отчет в формате json
