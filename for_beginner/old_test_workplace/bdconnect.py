#! /usr/bin/env python
# -*- coding: utf-8 -*-

import pymysql.cursors #
import json #




def get_controllers(dbkey,Id_role,Id_model):  
    role_id=Id_role
    module_id=Id_model    
    connection=pymysql.connect(host=dbkey[0],user=dbkey[1],password=dbkey[2],db=dbkey[3],charset=dbkey[4],cursorclass=pymysql.cursors.DictCursor )
    print('connect succesful!!!')
    try:
        with connection.cursor() as cursor:
            sql = """SELECT sys_controller.ID,sys_controller.MODULE_NAME as MODULE_NAME,rse_role_action.role_id as ROLE_ID,
CONCAT(sys_controller.page,'/',sys_controller.`action`) as URLLL,sys_controller.descr as DESCR, sys_controller.action as ACTION
FROM sys_controller,rse_role_action
WHERE sys_controller.ID=rse_role_action.action_id and CONCAT(sys_controller.page,'/',sys_controller.`action`)!='/' and
sys_controller.module_id={} and rse_role_action.role_id={} and sys_controller.action!='save' and sys_controller.action!='show'
ORDER BY sys_controller.id
"""
            cursor.execute(sql.format(module_id,role_id))
        data = cursor.fetchall()
        return(parsed_get_controllers(data))
    finally:
        connection.close()
        print('connect close!!!')

def parsed_get_controllers(arr):
        json_string=arr
        page=[]
        k=0
        cdescr=[]
        for i in json_string:
            print(str(i[u'URLLL']))
            page.append({'urll':'http://ecm4-test.slms.ru/' + str(i[u'URLLL']),'desc':str(i[u'DESCR']),'module':str(i[u'MODULE_NAME']),'action':str(i[u'ACTION'])})
            k=k+1
        print('Всего контроллеров: ' + str(k))
        return page

