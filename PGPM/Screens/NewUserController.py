#!/usr/bin/python
# This Python file uses the following encoding: utf-8
'''
@author: Federico Tersigni
'''
import justpy as jp
import sys

from Model.DAO.UtenteDAO import insertUtente

from Template.NewUserView import NewUserView

from Screens.Sessione import esisteSessione
from Screens.Sessione import creaSessione
from Screens.Sessione import showSessione
from Screens.Sessione import utenteLoggato
from Screens.Sessione import returnSessione

#Costanti delle Classi / Tailwind dei bottoni
agentiClasses = 'inline-block rounded w-32 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
agentiOnMouseOver = 'inline-block rounded w-32 h-16 bg-blue-600 m-2 text-white hover:bg-blue-400 focus:outline-white hover:text-white container'
buttonClasses = 'block rounded w-16 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
acceptClasses = 'block rounded w-16 h-16 m-2 bg-green-600 text-white hover:bg-green-300 focus:outline-white hover:text-gray-800'
rejectClasses = 'block rounded w-16 h-16 m-2 bg-red-600 text-white hover:bg-red-300 focus:outline-white hover:text-gray-800'
actionButtonClasses = 'block rounded w-32 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
#Codice della grafica della schermata di BACKEND

############################################

class NewUserController:


	async def newUserController(self,request):
		print('NEWUSERCONTROLLER----')
		session_id = request.session_id
		if not esisteSessione(session_id):
			creaSessione(session_id,False)
		else:
			#METTI TUTTI I DATI NELLE VARIABILI CHE MI SERVONO
			#IF PER VEDERE SE SIAMO LOGGATI O MENO
			if utenteLoggato(session_id):
				session = returnSessione(session_id)
			

			showSessione(session_id)

		session = returnSessione(session_id)

		wp = NewUserView(self.creaUtente,session)
		
		return wp

	def creaUtente(self,msg):
		print('creo nuovo utente' )
		nome=msg.form_data[0]['value']#nome
		email=msg.form_data[1]['value']#email
		password=msg.form_data[2]['value']#password
		confermaPassword=msg.form_data[3]['value']#conferma
		print(nome, email, password, confermaPassword)
		if(password == confermaPassword):
			print('inserisco utente')
			insertUtente(nome,email,password,0)
			msg.page.redirect = '/config/'
		else:
			print('password sbagliata')