#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys  
reload(sys)  
sys.setdefaultencoding('utf-8')
import pymysql.cursors #
import json #
import unittest
from difflib import ndiff
from itertools import izip_longest
from subprocess import check_output

class PythonOrgSearch(unittest.TestCase): 


    def testutils11(self):


        print("-----------------------------------------------------------------------------------")
        print(" ПРОВЕРКА ФАЙЛА /www/ecm4-mazda.prod/config/server.php") 
            
        configorigin = check_output(['php', '-r', 'echo json_encode(include "/home/pavel/Документы/AutoTests/Test/configs_for_testing/ecm4_all_server.php");'])
        config = check_output(['php', '-r', 'echo json_encode(include "/www/ecm4-all.prod/config/server.php");'])
        

        a = json.loads(configorigin)
        b = json.loads(config)


        f= open('logutils.txt','a') 

        f.write('||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||''\n')
       
        def valchange(d1, d2, parent=''):
            previous=0
            for key in d1.keys():
                try:
                    if d2[key] :
                        if isinstance(d1[key], list) or isinstance(d1[key], dict):
                            valchange(d1[key], d2[key])
                        else:
                            if str(d1[key]) != str(d2[key]):
                                f.write('Key:    | ' + str(key) + ' |    Value not equal A:    | ' + str(d1[key]) + ' |    B value:    | ' + str(d2[key]) + ' |   Previous key:    | ' + str(previous) +' |' + '\n')
                    else:
                        if key in d2:
                            f.write("Key not in that layer     | " + str(key) + ' |' + '\n')
                        else:
                            f.write('Key not exist:     | ' + str(key) + ' |' + '\n')
                except:
                    f.write('Exception parse key:     ' + str(key) + ' |' + '   value:' + str(d1[key]) + '\n')
                previous=key
        valchange(a,b)
        f.write("a/b ========================= b/a" + '\n')
        valchange(b,a)
        f.close()


if __name__ == "__main__": 
    unittest.main() 