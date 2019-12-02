#! /usr/bin/env python
# -*- coding: utf-8 -*-
import time
import pytest
# import allure
import methods_selenium as methods

from selenium import webdriver #Веб драйвер
from selenium.webdriver.common.action_chains import ActionChains #Эмулятор основных действий пользователя
from selenium.webdriver.common.keys import Keys  
from selenium.webdriver.common.by import By #??????
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.support import expected_conditions as EC 


def test_module_setup_driver():
    #!Авторизация
    driver = methods.init()                        
    driver = methods.authorization(driver,6)
    wait = WebDriverWait(driver, 500)
    wait.until(EC.presence_of_element_located((By.XPATH,"")))        
    driver.get('http://ecm4-master.slms.ru/crp_car_seller/show#id=15235')
    time.sleep(6)
    driver = methods.ButtonClick(driver,'Xpath',"//*[@id='StatusListBtn']/button[20]")


    # driver.close()
    assert 1==1
