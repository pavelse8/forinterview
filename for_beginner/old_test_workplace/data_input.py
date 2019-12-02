#! /usr/bin/env python
# -*- coding: utf-8 -*-
#?Модуль хранит информацию для ввода
def auth(role_id_in):
        conf={}
        role_id=role_id_in
        
        #ДЦ
    #? РОП role_id=6
        if role_id==6:
                conf ={'User_name': 'alexanderalexandrov', 'password': 'alexanderalexandrov1'}
                print("Авторизация под РОП")
    #? Логист ДЦ role_id=33
        if role_id==33:
                conf ={'User_name': 'alexanderalexandrov', 'password': 'alexanderalexandrov1'}
                print("Авторизация под Логист ДЦ")
    #? Инженер по гарантии ДЦ role_id=52
        if role_id==52:
                conf ={'User_name': 'singener', 'password': 'singener1'}
                print("Авторизация под Инженер по гарантии дц")
    #?Продавец role_id=1 Михаил Алексеев
        if role_id==1:
                conf ={'User_name': 'aem82', 'password': 'aem821'}
                print("Авторизация под Продавец")
        #Импортер:
    #?Региональный менеджер role_id=7 Максим Безус
        if role_id==7:
                conf ={'User_name': 'bezus', 'password': 'bezus1'}
                print("Авторизация под Региональный менеджер")
    #? Шеф импортера role_id=9
        if role_id==9:
                conf ={'User_name': 'uldasheva', 'password': 'uldasheva1'}
                print("Авторизация под Шеф")
    #? Логист дистрибьютора role_id=34
        if role_id==34:
                conf ={'User_name': 'tisaeva2', 'password': 'tisaeva21'}
                print("Авторизация под РОП")
    #? Инженер по гарантии импортера role_id=110
        if role_id==110:
                conf ={'User_name': 'lazarev', 'password': 'lazarev1'}
                print("Авторизация под РОП")
    #? Used car manager role_id=42
        if role_id==42:
                conf ={'User_name': 'eromanov', 'password': 'eromanov1'}
                print("Авторизация под РОП")
        #Админка
    #? Администратор Ефименков Павел role_id=5
        if role_id==5:
                conf ={'User_name': 'efimenkov', 'password': 'hgfdsa'}
                print("Авторизация под Администратор")
        return(conf)
    


        
def dbkey():
    #*host=dbkey[0],user=dbkey[1],password=dbkey[2],db=dbkey[3],charset=dbkey[4]
    dbkey=['178.159.252.191','root','Vb80k8P','ecm4-all-test','utf8']
    print(dbkey)
    return dbkey

