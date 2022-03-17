#!/usr/bin/python
# This Python file uses the following encoding: utf-8
'''
@author: Federico Tersigni
'''
import os
import sys
from os import listdir
from os.path import isfile, join
import glob
import justpy as jp
import Screens as scr
from Screens.Sessione import esisteSessione
from Screens.Sessione import creaSessione
from Screens.Sessione import showSessione
from Screens.Sessione import utenteLoggato
from Screens.Sessione import returnSessione
from Screens.Sessione import esisteChiave
from Screens.Sessione import returnElemento
from Screens.Sessione import addElementoSessione
from Screens.Sessione import cambiaAttributoAgente
from Screens.Sessione import eliminaAgente
from Screens.Sessione import addAgenteInSessione
from Screens.Sessione import cambiaAttributo

from Template.ProfileView import ProfileView

from Model.DAO.UtenteDAO import updateEmail
from Model.DAO.UtenteDAO import updatePassword
from Model.DAO.UtenteDAO import checkPassword
from Model.DAO.UtenteDAO import deleteUtente



class ProfileScreen:

	async def profileScreen(self,request):
		s_id = request.session_id
		print('Profilo')
		session={}

		if not esisteSessione(s_id):
			creaSessione(s_id,False)
		else:
			if utenteLoggato(s_id):
				session = returnSessione(s_id)

		session = returnSessione(s_id)
		wp = ProfileView(self.cambioEmail,self.cambioPassword, self.deleteAccount,session)
		return wp

	#Edit Email
	def cambioEmail(self,msg):
		print('cambio email')
		session={}
		s_id = msg.session_id
		#print(msg.form_data)
		credenziali=[]
		for field in msg.form_data:
			if field['type'] != 'submit':
				credenziali.append(field.value)
		print(credenziali)

		session = returnSessione(s_id)
		#print('Session ---')
		#print(session)
		idUtente=session['utente'][0]
		#Fai il check della password, se è == a quella registrata, cambia email
		#print(session['utente'], ' <--- utente')
		check = checkPassword(idUtente)
		print(check, '<-- ?? ')
		if check == credenziali[0]:
			print('Password corretta')
			updateEmail(idUtente, credenziali[1]) # corretta
			cambiaAttributo(s_id,'utente',2,credenziali[1])
		else:
			print('password non corretta')
		print('Finito, faccio il redirect')
		msg.page.redirect = '/profile/'



	#Edit Password
	def cambioPassword(self,msg):
		print('cambio password')
		session={}
		s_id = msg.session_id
		#print(msg.form_data)
		credenziali=[]
		for field in msg.form_data:
			if field['type'] != 'submit':
				credenziali.append(field.value)
		print(credenziali)

		session = returnSessione(s_id)
		#print('Session ---')
		#print(session)
		idUtente=session['utente'][0]
		#Fai il check della password, se è == a quella registrata, cambia email
		#print(session['utente'], ' <--- utente')
		check = checkPassword(idUtente)
		print(check, '<-- ?? ')
		if check == credenziali[0]:
			print('Password corretta')
			updatePassword(idUtente, credenziali[1]) # corretta
			cambiaAttributo(s_id,'utente',3,credenziali[1])
		else:
			print('password non corretta')
		print('Finito, faccio il redirect')
		msg.page.redirect = '/profile/'

	#Cancella Account + cancella sessione e reindirizza
	def deleteAccount(self,msg):
		print('cancella account')
		s_id = msg.session_id
		print('?', msg.target)
		print('-',msg.target.idUtente, type(msg.target.idUtente))
		xid = msg.target.idUtente
		print(xid , '<-----')
		print('?')
		deleteUtente(xid)
		print('Cancella Sessione')
		#cancella sessione
		cancellaSessione(s_id)
		print('?')
		msg.page.redirect='/start/'