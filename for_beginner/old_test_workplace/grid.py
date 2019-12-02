#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time
import pytest
# import allure
import methods_selenium as methods
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from selenium import webdriver #Веб драйвер
from selenium.webdriver.common.action_chains import ActionChains #Эмулятор основных действий пользователя
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


def test_New_company_button(driver, i):
    

    f = methods.log_open() # Открытие лог файла
    methods.printNametest(" Теcт грида на странице :" + i['urll']) # Запись названия теста в лог

    time.sleep(4)

    # Добавление колонок
    try:
        element = driver.find_element_by_xpath("(//button[contains(@class, 'btn btn-default modal-customize')])[1]")
        driver.execute_script("arguments[0].click();", element)
        all_options = element.find_elements_by_tag_name("option")
        for option in all_options:
            print("Value is: %s" % option.get_attribute("value"))
            option.click()
        driver.execute_script("arguments[0].click();", driver.find_element_by_name("btn-add"))
        driver.execute_script("arguments[0].click();", driver.find_element_by_xpath("//*[@id='modal_customizable']/div/div/div[3]/button"))
    except:
        f.write("В гриде не предусмотрен выбор колонок")


    #Получение всех сортировок
    try:
        time.sleep(4)
        sortings = driver.find_elements_by_xpath("(//*[@class='grid-header'])[1]//*[@class='pointer']")
    except:
        time.sleep(4)
        sortings = driver.find_elements_by_xpath("(//*[@class='grid-header'])[1]//*[@class='pointer']")

    for sort in sortings:
        time.sleep(1)

        # TODO ____________Взять поиск ошибки из файла методс_____________

        driver.execute_script("arguments[0].click();", sort)
        time.sleep(1)
        try:
            a = driver.find_element_by_class_name('alert-message').text
            if a:
                f.write("Ошибка в гриде на странице URL: " + i['urll'] + '\n')
                driver.save_screenshot("Грид ошибка - Контроллер:" + i['desc'] + '(' + i['module'] + ')''ff.png')
                break
        except:
            try:
                time.sleep(3)
                a = driver.find_element_by_class_name('alert-message')
                if a:
                    f.write("Ошибка в гриде на странице URL: " + i['urll'] + '\n')
                    driver.save_screenshot("Грид ошибка - Контроллер:" + i['desc'] + '(' + i['module'] + ')''ff.png')
                    break
            except:
                a = '3'

    f.write("Тест грида окончен" + '\n')
    f.close()

    return driver

   