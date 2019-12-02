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
from xvfbwrapper import Xvfb

def test_module_setup_driver():
    
    #!Включение виртуального дисплея
    vdisplay = Xvfb(width=2400 , height=1200)
    vdisplay.start()
    time.sleep(3)
    methods.printNametest("Тест по прохождению контроллеров")  
    # # ДЦ:
    # methods.printNametest("Тест по прохождению контроллеров - УРОВЕНЬ ДЦ")  
    # #? РОП (6)
    # methods.printNametest("Тест по прохождению контроллеров - УРОВЕНЬ ДЦ - РОП")  
    # driver = methods.init()
    # driver = methods.authorization(driver,6)
    # driver = methods.around_controllers(driver,6)
    # driver.close()
    # #? Логист ДЦ(33)
    # methods.printNametest("Тест по прохождению контроллеров - УРОВЕНЬ ДЦ - ЛОГИСТ ДЦ")  
    # driver = methods.init()
    # driver = methods.authorization(driver,33)
    # driver = methods.around_controllers(driver,33)
    # driver.close()
    # #? Продавец(1)
    # methods.printNametest("Тест по прохождению контроллеров - УРОВЕНЬ ДЦ- ПРОДАВЕЦ")  
    # driver = methods.init()
    # driver = methods.authorization(driver,1)
    # driver = methods.around_controllers(driver,1)
    # driver.close()
    # #? Инженер по гарантии ДЦ(52)
    # methods.printNametest("Тест по прохождению контроллеров - УРОВЕНЬ ДЦ - ИНЖЕНЕР ПО ГАРАНТИИ ДЦ")  
    # driver = methods.init()
    # driver = methods.authorization(driver,52)
    # driver = methods.around_controllers(driver,52)
    # driver.close()
   
    
    
    # #? ИМПОРТЕР:
    methods.printNametest("Тест по прохождению контроллеров - УРОВЕНЬ ИМПОРТЕР")  
    #?  Региональный менеджер (7)
    methods.printNametest("Тест по прохождению контроллеров - УРОВЕНЬ ИМПОРТЕР- РЕГИОНАЛЬНЫЙ МЕНЕДЖЕР")  
    driver = methods.init()
    driver = methods.authorization(driver,7)
    driver = methods.around_controllers(driver,7)
    driver.close()
    #?  Шеф(9)                         (9,2)
    methods.printNametest("Тест по прохождению контроллеров - УРОВЕНЬ ИМПОРТЕР - ШЕФ")  
    driver = methods.init()
    driver = methods.authorization(driver,9)
    driver = methods.around_controllers(driver,9)
    driver.close()
    #? Used_car_manager(42)       (42,7)
    methods.printNametest("Тест по прохождению контроллеров - УРОВЕНЬ ИМПОРТЕР - USED CAR MANAGER")  
    driver = methods.init()
    driver = methods.authorization(driver,42)
    driver = methods.around_controllers(driver,42)
    driver.close()
    #? Логист дистрибьютора(34)          (34,5)
    methods.printNametest("Тест по прохождению контроллеров - УРОВЕНЬ ИМПОРТЕР - ЛОГИСТ ДИСТРИБЬЮТОРА")  
    driver = methods.init()
    driver = methods.authorization(driver,34)
    driver = methods.around_controllers(driver,34)
    driver.close()
    #? Инженер по гарантии(110)         (110,6)
    methods.printNametest("Тест по прохождению контроллеров - УРОВЕНЬ ИМПОРТЕР - ИНЖЕНЕР ПО ГАРАНТИИ")  
    driver = methods.init()
    driver = methods.authorization(driver,110)
    driver = methods.around_controllers(driver,110)
    driver.close()


    vdisplay.stop()
    assert 1==1
