#!/usr/bin/python
# This Python file uses the following encoding: utf-8
'''
@author: Federico Tersigni
'''

import os
import sys
from os import listdir
from os.path import isfile, join, basename
import glob

import justpy as jp
from Template.ConfigView import ConfigView
from Model.DAO.UtenteDAO import validazione
from Model.DAO.RunDAO import listaRunUtente
from Model.DAO.RunDAO import deleteRun
from Model.DAO.DirectoryDAO import getDirectory
from Model.DAO.AgenteDAO import listaAgentiDir
from Model.Run import Run
from Model.Agente import Agente
from Model.Directory import Directory

from Screens.Sessione import esisteSessione
from Screens.Sessione import creaSessione
from Screens.Sessione import showSessione
from Screens.Sessione import addElementoSessione
from Screens.Sessione import returnSessione
from Screens.Sessione import cancellaSessione
from Screens.Sessione import utenteLoggato

#import sqlite3 as sql

#Costanti delle Classi / Tailwind dei bottoni
agentiClasses = 'inline-block rounded w-32 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
agentiOnMouseOver = 'inline-block rounded w-32 h-16 bg-blue-600 m-2 text-white hover:bg-blue-400 focus:outline-white hover:text-white container'
buttonClasses = 'block rounded w-16 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
acceptClasses = 'block rounded w-16 h-16 m-2 bg-green-600 text-white hover:bg-green-300 focus:outline-white hover:text-gray-800'
rejectClasses = 'block rounded w-16 h-16 m-2 bg-red-600 text-white hover:bg-red-300 focus:outline-white hover:text-gray-800'
actionButtonClasses = 'block rounded w-32 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
#Codice della grafica della schermata di Configurazione


############################################


class ConfigScreen:

	async def configScreen(self,request): # GIUSTA
		
		print('CONFIG-SCREEN ')
		session_id = request.session_id
		session = {}
		listaD=[]
		lista=[]
		if not esisteSessione(session_id):
			creaSessione(session_id,False)
		else:
			if utenteLoggato(session_id):
				print('Connessi.')
				u = returnSessione(session_id)
				#print(u)
				lista = listaRunUtente(u['utente'][0])
				#print(type(lista))
				#print('mostro Lista Run Utente')
				listaD = getDirectory(u['utente'][0])

				#for x in lista:
				#	value = x.getId()
				#	y=getDirectory(value)
				#	listaD.append(y)
					

		
		session = returnSessione(session_id)
		wp = ConfigView(listaD,lista,self.login,self.savePath,self.logout,self.sceltaRunCanc,self.sceltaPath,session)
		return wp

	#Funzioni del configScreen da settare

	async def login(self,msg):
		print('login ------- ')
		credenziali=[]
		for field in msg.form_data:
			#print('Guardo il field', field['type'])
			#print('------> ', field)
			if field['type'] == 'text':
				#print('--------->',field.value)
				credenziali.append(field.value)
			elif field['type'] == 'password':
				#print('--------->',field.value)
				credenziali.append(field.value)

		#print('Credenziali Inserite ::::: ', credenziali)
		print('###')
		verifica = validazione(credenziali[0],credenziali[1])
		print('verifica:::: ', verifica)
		#print('Verifica -----> ',verifica)
		if verifica is not None:
			print('CONNESSO!')
			session_id = msg.session_id
			chiave='logged_in'
			addElementoSessione(session_id,chiave,True)
			addElementoSessione(session_id,'utente',verifica)

			msg.page.redirect = '/config/'

		else:
			print('NON SEI CONNESSO')
			msg.target.classes = 'block border-2 border-red-600 m-10 p-2'
		

	def logout(self,msg):
		print('logout---')

		session_id = msg.session_id

		cancellaSessione(session_id)
		
		msg.page.redirect='/config/'
		

	async def savePath(self,msg):
		#print('Salvataggio del path')
		#print(msg.form_data[0].value)
		_path = msg.form_data[0].value
		#print(msg.form_data)
		_nome = msg.form_data[1].value
		#Questa variabile è il path scritto dall'utente nel programma
		s_id = msg.session_id
		addElementoSessione(s_id,'path',_path)
		addElementoSessione(s_id,'nome_path',_nome)
		#salvo TUTTI gli agenti presenti in quel path nella sessione
		listaAgenti={}#Sarà un dizionario
		#print('dopo listaAgenti')
		searching = _path +'*.py'

		a = [os.path.basename(x) for x in glob.glob(searching)]
		#print('dopo FileGlob')
		for nome in a:
			#Colore, stato, filtro
			listaAgenti[nome] = ['#444444', 1,1]
		#print('provo ad aggiungere agenti')
		addElementoSessione(s_id,'agenti',listaAgenti)

		msg.page.redirect ='/start/'

	async def sceltaRunCanc(self,msg): #funziona
		print('---')
		#print(msg.form_data[0].value)
		#Cancella Run specificata dal suo id.
		idRun = msg.form_data[0].value
		deleteRun(idRun)
		msg.page.redirect='/config/'

	def sceltaPath(self,msg):
		print('SCELTA PATH')
		#Array : [id, path]
		s_id = msg.session_id
		#dirList = msg.form_data[0].value 
		listaAgenti = {}
		#locat = dirList[2:]

		
		#print(msg.form_data)
		dirId = msg.form_data[1].value
		dirPath = msg.form_data[2].value
		dirNome = msg.form_data[3].value
		dirUtenteId = msg.form_data[4].value

		
		
		#Funzione che carica tutte le info della specifica dir
		#Query che mi mette tutti gli agenti della directory nella sessione con i loro attr
		#Salvo anche il path nella sessione
		
		xList = listaAgentiDir(dirId)
		print(xList)
		for x in xList:
			pathExist = os.path.exists(dirPath+x.getNome())
			if pathExist:
				print('esiste')
				listaAgenti[x.getNome()]=[x.getColore(),x.getStato(),x.getFiltro()]

		#Aggiungo Path e listaAgenti alla sessione
		
		addElementoSessione(s_id,'path',dirPath)
		addElementoSessione(s_id,'nome_path',dirNome)
		addElementoSessione(s_id,'agenti',listaAgenti)

		print('############## FINE SCELTA PATH')

		msg.page.redirect='/start/'
