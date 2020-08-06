# -*- coding: utf-8 -*-
import os, sys
import json
import datetime
import time
import trylib

# папка параметр из либы
# проверка папки из либы
# проверка длины из либы
# создание обьектного жсона
#  чтение и отрытие жсона можно тоже в либы

if len(sys.argv)>1 :
	pa=sys.argv[1]
else:
	pa="vps"

bpath=trylib.yfolder(pa)
 
print(trylib.dtnow("t"))
print(trylib.dtnow("d"))
 

for t in range(9999):
	inp =  input("текст: ")
	fname=trylib.yfile(inp,bpath)
	#print ("z"+fname)
	data={"vp":{}}
	data["vp"]["text"]=inp.strip()
	data["vp"]["tadd"]=trylib.dtnow("t")
	data["vp"]["dadd"]=trylib.dtnow("d")
	
	fupana=bpath+fname
	#print ("z"+fupana)
	#print (data)
	trylib.savej(fupana,data)
	
	os.system('cls||clear')

