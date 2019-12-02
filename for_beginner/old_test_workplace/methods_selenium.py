#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import data_input
import locators
import bdconnect
import time
import datetime
import grid

from selenium import webdriver #Веб драйвер
from selenium.webdriver.common.action_chains import ActionChains #Эмулятор основных действий пользователя
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By #??????
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

reload(sys)
sys.setdefaultencoding('utf8')

def log_open():
    f= open('log.txt','a')
    return f

def log_close(f):
    f.close

def init():#*Инициализация драйвера
    driver=webdriver.Firefox()
    return driver

def authorization(driver,role_id):#*Авторизация
    f = log_open()
     #? ДЦ:
    #? Продажа - 2 / РОП (6)                        (6,2)
    #? Кароператор - 7 / РОП(6)                     (6,7)
    #? Обучение - 4 / РОП(6)                        (6,4)
    #? Склад - 5/ Логист ДЦ(33)                     (33,5)
    #? Сервис - 6/ Инженер по гарантии ДЦ(52)       (52,6)
    #? ИМПОРТЕР:
    #? Продажа - 2 / Шеф(9)                         (9,2)
    #? Кароператор - 7 / Used_car_manager(42)       (42,7)
    #? Обучение - 4 / Шеф(9)                        (9,4)
    #? Склад - 5/ Логист дистрибьютора(34)          (34,5)
    #? Сервис - 6/ Инженер по гарантии(110)         (110,6)
    if role_id == 6:
            f.write("Авторизация под ролью РОП :  " + str(role_id) + '\n')
    if role_id == 33:
            f.write("Авторизация под ролью Логист ДЦ:  " + str(role_id) + '\n')
    if role_id == 52:
            f.write("Авторизация под ролью Инженер по гарантии ДЦ:  " + str(role_id) + '\n')
    if role_id == 9:
            f.write("Авторизация под ролью Шеф:  " + str(role_id) + '\n')
    if role_id == 42:
            f.write("Авторизация под ролью Used_car_manager:  " + str(role_id) + '\n')
    if role_id == 34:
            f.write("Авторизация под ролью Логист дистрибьютора:  " + str(role_id) + '\n')
    if role_id == 110:
            f.write("Авторизация под ролью Инженер по гарантии:  " + str(role_id) + '\n')
    if role_id == 5:
            f.write("Авторизация под ролью Администратор:  " + str(role_id) + '\n')

    try:
        driver.get(locators.page("Авторизация"))

        elem = driver.find_element_by_name("username")
        elem.send_keys(data_input.auth(role_id)['User_name'])
        elem = driver.find_element_by_name("password")
        elem.send_keys(data_input.auth(role_id)['password'])
        elem.send_keys(Keys.ENTER)
        time.sleep(2)

    except Exception as e:
        f.write("Не удалось авторизоваться" + '\n')
        f.write(e + '\n')
    f.close()
    return driver

def deauthorization(driver):#Выход из аккаунта
    driver.find_element_by_class_name("btn userinfo-btn dropdown-toggle").click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='header']/nav/div/div/div/div/div[4]/div[1]/ul/li/a")
    return driver

def get_controllers(Test_role_id,Test_module_id):#*Получение контроллеров по модулю и роли
    #?bdconnect.get_controllers(Соединение с базой,ID_роли,ID_модуля)
    listcontr=bdconnect.get_controllers(data_input.dbkey(), str(Test_role_id), str(Test_module_id))
    f = log_open()
    f.write("Контроллеры роли " + str(Test_role_id) + ", модуля " + str(Test_module_id) + '\n')
    for i in listcontr:
        f.write(i['urll'] + '\n')
    f.close()
    return listcontr

def find_error_on_page(driver,i):
    f =log_open()
    if len(driver.find_elements_by_tag_name('pre')) > 0:
        if "Class not found!" in driver.page_source:
            f.write("Ошибка! Класс не найден! URL: " + i['urll'] + ' Контроллер: ' + i['desc'] + '(' + i['module']+')' + '\n')
            driver.save_screenshot("Контроллер:" + i['desc'] + '(' + i['module']+')''ff.png')
        else:
            if "В доступе отказано!" in driver.page_source:
                f.write("В доступе отказано! URL: " + i['urll'] + ' Контроллер: ' + i['desc'] + '(' + i['module']+')' + '\n')
                driver.save_screenshot("Контроллер:" + i['desc'] + '(' + i['module']+')''ff.png')
            else:
                f.write("Ошибка на странице! Необходимо проверить URL: " + i['urll'] + ' Контроллер: ' + i['desc'] + '(' + i['module']+')' + '\n')
                driver.save_screenshot("Контроллер:" + i['desc'] + '(' + i['module']+')''ff.png')
    time.sleep(2)

    try:
        a=driver.find_element_by_class_name('alert-message').text
        if a:
            f.write("Ошибка!Модальное окно на странице URL: " + i['urll'] + ' Контроллер: ' + i['desc'] + '(' + i['module']+')' + '\n')
            driver.save_screenshot("Контроллер:" + i['desc'] + '(' + i['module']+')''ff.png')
    except:
        try:
            time.sleep(2)
            a=driver.find_element_by_class_name('alert-message').text
            if a:
                f.write("Ошибка!Модальное окно на странице URL: " + i['urll'] + ' Контроллер: ' + i['desc'] + '(' + i['module']+')' + '\n')
                driver.save_screenshot("Контроллер:" + i['desc'] + '(' + i['module']+')''ff.png')
        except:
            a='3'
    f.close()

    if i['action'] == 'list':
        driver = grid.test_New_company_button(driver, i)

    return driver

def around_controllers(driver,role_id): #*Переходит на контроллеры полученные в get_controller и проверяет их

    #? ДЦ:
    #? Продажа - 2 / РОП (6)                        (6,2)
    #? Кароператор - 7 / РОП(6)                     (6,7)
    #? Обучение - 4 / РОП(6)                        (6,4)
    #? Склад - 5/ Логист ДЦ(33)                     (33,5)
    #? Сервис - 6/ Инженер по гарантии ДЦ(52)       (52,6)
    #? ИМПОРТЕР:
    #? Продажа - 2 / Шеф(9)                         (9,2)
    #? Кароператор - 7 / Used_car_manager(42)       (42,7)
    #? Обучение - 4 / Шеф(9)                        (9,4)
    #? Склад - 5/ Логист дистрибьютора(34)          (34,5)
    #? Сервис - 6/ Инженер по гарантии(110)         (110,6)
    if role_id==6: #*Роп
        #Корпоративные сделки
        f =log_open()
        f.write("_____________________________________________________________________" + '\n')
        f.write("МОДУЛЬ КОРПОРАТИВНЫЕ СДЕЛКИ" + '\n')
        f.close()
        for i in get_controllers(role_id,19):
                a=False
                time.sleep(1)
                driver.get(i['urll'])
                find_error_on_page(driver,i)
        return driver
        #Продажа
        f =log_open()
        f.write("_____________________________________________________________________" + '\n')
        f.write("МОДУЛЬ ПРОДАЖА ДЦ" + '\n')
        f.close()
        for i in get_controllers(role_id,2):
                a=False
                time.sleep(1)
                driver.get(i['urll'])
                find_error_on_page(driver,i)
        #Кароператор
        f =log_open()
        f.write("_____________________________________________________________________" + '\n')
        f.write("МОДУЛЬ КАРОПЕРАТОР ДЦ" + '\n')
        f.close()
        for i in get_controllers(role_id,7):
                a=False
                time.sleep(1)
                driver.get(i['urll'])
                find_error_on_page(driver,i)
        #Обучение
        f =log_open()
        f.write("_____________________________________________________________________" + '\n')
        f.write("МОДУЛЬ ОБУЧЕНИЕ ДЦ" + '\n')
        f.close()
        for i in get_controllers(role_id,4):
                a=False
                time.sleep(1)
                driver.get(i['urll'])
                find_error_on_page(driver,i)
        return driver

    if role_id==33: #*Логист ДЦ
        #Склад
        f =log_open()
        f.write("_____________________________________________________________________" + '\n')
        f.write("МОДУЛЬ СКЛАД ДЦ" + '\n')
        f.close()
        for i in get_controllers(role_id,5):
                a=False
                time.sleep(1)
                driver.get(i['urll'])
                find_error_on_page(driver,i)
        return driver

    if role_id==52: #*Инженер по гарантии ДЦ
        #Сервис
        f =log_open()
        f.write("_____________________________________________________________________" + '\n')
        f.write("МОДУЛЬ СЕРВИС ДЦ" + '\n')
        f.close()
        for i in get_controllers(role_id,6):
                a=False
                time.sleep(1)
                driver.get(i['urll'])
                find_error_on_page(driver,i)
        return driver

    if role_id==1: #*Продавец
        #Продажа
        f =log_open()
        f.write("_____________________________________________________________________" + '\n')
        f.write("МОДУЛЬ ПРОДАЖА ДЦ" + '\n')
        f.close()
        for i in get_controllers(role_id,2):
                a=False
                time.sleep(1)
                driver.get(i['urll'])
                find_error_on_page(driver,i)
        #Кароператор
        f =log_open()
        f.write("_____________________________________________________________________" + '\n')
        f.write("МОДУЛЬ КАРОПЕРАТОР ДЦ" + '\n')
        f.close()
        for i in get_controllers(role_id,7):
                a=False
                time.sleep(1)
                driver.get(i['urll'])
                find_error_on_page(driver,i)
        #Обучение
        f =log_open()
        f.write("_____________________________________________________________________" + '\n')
        f.write("МОДУЛЬ ОБУЧЕНИЕ ДЦ" + '\n')
        f.close()
        for i in get_controllers(role_id,4):
                a=False
                time.sleep(1)
                driver.get(i['urll'])
                find_error_on_page(driver,i)
        return driver

    if role_id==9: #*Шеф
        #Продажа
        f =log_open()
        f.write("_____________________________________________________________________" + '\n')
        f.write("МОДУЛЬ ПРОДАЖА ИМПОРТЕР" + '\n')
        f.close()
        for i in get_controllers(role_id,2):
                a=False
                time.sleep(1)
                driver.get(i['urll'])
                find_error_on_page(driver,i)
        return driver

        #Обучение
        f =log_open()
        f.write("_____________________________________________________________________" + '\n')
        f.write("МОДУЛЬ ОБУЧЕНИЕ ИМПОРТЕР" + '\n')
        f.close()
        for i in get_controllers(role_id,4):
                a=False
                time.sleep(1)
                driver.get(i['urll'])
                find_error_on_page(driver,i)
        return driver

    if role_id==42: #*Used car manager

        #Корпоративные сделки
        f =log_open()
        f.write("_____________________________________________________________________" + '\n')
        f.write("МОДУЛЬ КОРПОРАТИВНЫЕ СДЕЛКИ" + '\n')
        f.close()
        for i in get_controllers(role_id,19):
                a=False
                time.sleep(1)
                driver.get(i['urll'])
                find_error_on_page(driver,i)
        return driver

        #Кароператор
        f =log_open()
        f.write("_____________________________________________________________________" + '\n')
        f.write("МОДУЛЬ КАРОПЕРАТОР" + '\n')
        f.close()
        for i in get_controllers(role_id,7):
                a=False
                time.sleep(1)
                driver.get(i['urll'])
                find_error_on_page(driver,i)
        return driver

    if role_id==34: #*Логист дистрибьютора
        #Склад
        f=log_open()
        f.write("_____________________________________________________________________" + '\n')
        f.write("МОДУЛЬ СКЛАД" + '\n')
        f.close()
        for i in get_controllers(role_id,5):
                a=False
                time.sleep(1)
                driver.get(i['urll'])
                find_error_on_page(driver,i)
        return driver

    if role_id==110: #*Инжинер по гарантии
        #Сервис
        f=log_open()
        f.write("_____________________________________________________________________" + '\n')
        f.write("МОДУЛЬ СЕРВИС ИМПОРТЕР" + '\n')
        f.close()
        for i in get_controllers(role_id,6):
                a=False
                time.sleep(1)
                driver.get(i['urll'])
                find_error_on_page(driver,i)
        return driver

    if role_id==7: #*Региональный менеджер
        #Продажа
        f =log_open()
        f.write("_____________________________________________________________________" + '\n')
        f.write("МОДУЛЬ ПРОДАЖА ИМПОРТЕР" + '\n')
        f.close()
        for i in get_controllers(role_id,2):
                a=False
                time.sleep(1)
                driver.get(i['urll'])
                find_error_on_page(driver,i)
        #Кароператор
        f =log_open()
        f.write("_____________________________________________________________________" + '\n')
        f.write("МОДУЛЬ КАРОПЕРАТОР ДЦ" + '\n')
        f.close()
        for i in get_controllers(role_id,7):
                a=False
                time.sleep(1)
                driver.get(i['urll'])
                find_error_on_page(driver,i)
        #Обучение
        f =log_open()
        f.write("_____________________________________________________________________" + '\n')
        f.write("МОДУЛЬ ОБУЧЕНИЕ ДЦ" + '\n')
        f.close()
        for i in get_controllers(role_id,4):
                a=False
                time.sleep(1)
                driver.get(i['urll'])
                find_error_on_page(driver,i)
        return driver

    if role_id==5: #*АДМИН
        f =log_open()
        f.write("_____________________________________________________________________" + '\n')
        f.write("МОДУЛЬ АДМИН" + '\n')
        f.close()
        for i in get_controllers(role_id,1):
                a=False
                time.sleep(1)
                driver.get(i['urll'])
                find_error_on_page(driver,i)
        return driver

        f =log_open()
        f.write("_____________________________________________________________________" + '\n')
        f.write("МОДУЛЬ АДМИН" + '\n')
        f.close()
        for i in get_controllers(role_id,11):
                a=False
                time.sleep(1)
                driver.get(i['urll'])
                find_error_on_page(driver,i)
        return driver

def around_controllers_gaz(driver,role_id): #*Переходит на контроллеры полученные в get_controller и проверяет их

    #? ДЦ:
    #? РОП (6)

    #? Газ:
    #? Шеф(9)

    if role_id==6: #*Роп
        #Корпоративные сделки
        f =log_open()
        f.write("_____________________________________________________________________" + '\n')
        f.write("МОДУЛЬ КОРПОРАТИВНЫЕ СДЕЛКИ" + '\n')
        f.close()
        for i in get_controllers(role_id,19):
                a=False
                time.sleep(1)
                driver.get(i['urll'])
                find_error_on_page(driver,i)
        return driver

    if role_id==9: #*Шеф
        #Корпоративные сделки
        f =log_open()
        f.write("_____________________________________________________________________" + '\n')
        f.write("МОДУЛЬ КОРПОРАТИВНЫЕ СДЕЛКИ" + '\n')
        f.close()
        for i in get_controllers(role_id,19):
                a=False
                time.sleep(1)
                driver.get(i['urll'])
                find_error_on_page(driver,i)
        return driver

def ButtonClick(driver,typeSelector,Selector):

        if typeSelector=="CLASS_NAME":
                try:
                        wait = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME,Selector)))
                        driver.execute_script("arguments[0].click();", wait)
                except:
                        f = log_open()

                        f.write("Элемент не кликабелен" + '\n' + '\n')

        if typeSelector=="XPATH":
                try:
                        wait = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,Selector)))
                        driver.execute_script("arguments[0].click();", wait)
                except:
                        f = log_open()

                        f.write("Элемент не кликабелен" + '\n' + '\n')

        if typeSelector=="ID":
                try:
                        wait = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID,Selector)))
                        driver.execute_script("arguments[0].click();", wait)
                except:
                        f = log_open()

                        f.write("Элемент не кликабелен" + '\n' + '\n')

        if typeSelector=="NAME":
                try:
                        wait = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME,Selector)))
                        driver.execute_script("arguments[0].click();", wait)
                except:
                        f = log_open()

                        f.write("Элемент не кликабелен" + '\n' + '\n')

        return driver

def JSButtonClick(driver,Selector):

        driver.execute_script("arguments[0].click();", Selector)
        return driver

def TextInput(driver,Selector,text):
        wait = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,Selector)))
        wait.send_keys(text.decode('utf-8'))
        return driver

def Selectchoose(driver,Selector, Select):
        wait = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH,Selector)))

def printNametest(name):
    f = log_open()
    now = datetime.datetime.now()
    f.write("*********************************************************************" + '\n')
    f.write("************* НОВЫЙ ТЕСТ : " + name + " ******************" + '\n' + '\n')
    f.write("*************Начало теста в : " +str(now)+ " ******************" + '\n' + '\n')

    f.close()