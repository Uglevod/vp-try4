# -*- coding: utf-8 -*-
import os, sys
import json
import datetime
import time
import os.path

def savej(fpn,data):
	 
	with open(fpn, "w",encoding="utf-8") as write_file:
			json.dump(data, write_file, ensure_ascii=False)
			

def yfoldfile(fpa):
# проверка - это диретория выписки ?
	fpf=fpa+"vp_folder.tag"
	 
	if  os.path.isfile(fpf) :
		c=5
	else:
		my_file = open(fpf, 'w')
		my_file.write(" ")
		my_file.close()


def yfile(inp,fpath):
# проверка длинны и наличия копии
	if len(inp)>100:
		inpj = inp.strip()[0:101] + '___ .json'
	else:	
		inpj = inp.strip() + '.json'

	check_file = os.path.exists(fpath+inpj) 
	
	if check_file:
		inp =  input("есть такой - назови по другому: ")
		if len(inp)>100:
			inpj = inp.strip()[0:101] + '___ .json'
		
		inpj = inp + '.json'
	return inpj


def yfolder(fp):
	# провека папки на существование
	# если есть то завершение работы = если есь то ок
	# если нет то создаем 
	# пишем фаил vpfolder.tag
	npa=fp.strip()
	basepa="./"
	osnpa="vps/"

	if npa!="":
		osnpa=npa
	
	fpath=basepa+osnpa

	if os.path.exists(fpath):
		#print(os.path.exists(fpath))
		#print("Каталог "+fpath+" существует")
		c=5
	else:
		try:
			os.mkdir(npa)
		except OSError:
			print ("Создать директорию %s не удалось" % fpath)	
	yfoldfile(fpath+"/")
	return fpath+"/"


def dtnow(key):
	now=datetime.datetime.now()
	 
	if key=="t":
		ret=now.strftime("%H:%M") 
	if key=="d":
		ret=now.strftime("%d.%m.%y") 
	return ret
