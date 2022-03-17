#!/usr/bin/python
# This Python file uses the following encoding: utf-8
'''
@author: Federico Tersigni
'''
import justpy as jp
import sys


from Template.BackendUtenteView import BackendUtenteView
from Model.DAO.UtenteDAO import listaUtente
from Model.DAO.UtenteDAO import deleteUtente
from Model.DAO.UtenteDAO import updateRuolo

from Screens.Sessione import esisteSessione
from Screens.Sessione import creaSessione
from Screens.Sessione import showSessione
from Screens.Sessione import addElementoSessione
from Screens.Sessione import returnSessione
from Screens.Sessione import utenteLoggato


#Costanti delle Classi / Tailwind dei bottoni
agentiClasses = 'inline-block rounded w-32 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
agentiOnMouseOver = 'inline-block rounded w-32 h-16 bg-blue-600 m-2 text-white hover:bg-blue-400 focus:outline-white hover:text-white container'
buttonClasses = 'block rounded w-16 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
acceptClasses = 'block rounded w-16 h-16 m-2 bg-green-600 text-white hover:bg-green-300 focus:outline-white hover:text-gray-800'
rejectClasses = 'block rounded w-16 h-16 m-2 bg-red-600 text-white hover:bg-red-300 focus:outline-white hover:text-gray-800'
actionButtonClasses = 'block rounded w-32 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
#Codice della grafica della schermata di BACKEND

############################################

class BackendUtenteScreen:


	async def backendUtenteScreen(self,request):
		print('BACKEND UTENTE SCREEN')
		#print('--- Prova Lista Utente ----')
		listaUtenti = listaUtente()

		session_id = request.session_id
		if not esisteSessione(session_id):
			creaSessione(session_id,False)
			request.redirect('/')

		else:
			if utenteLoggato(session_id):
				session = returnSessione(session_id)
			else:
				request.redirect('/')

		session = returnSessione(session_id)
		wp = BackendUtenteView(listaUtenti,self.cancella,self.cambioGrado,session)
		return wp

	def cancella(self,msg):
		print('cancella elemento')
		xid = list(msg.target.idUtente)
		deleteUtente(xid[0])
		msg.page.redirect = '/backend/gestioneUtente/'

	def cambioGrado(self,msg):
		print('modifica grado utente')
		xid = list(msg.target.idUtente)
		print('dopo xid ')

		xgrado = list(msg.target.ruolo)
		print(xgrado, '------- xgrado')
		print(type(xgrado[0]))
		grade = int(xgrado[0])
		print('---->', grade, ' || ', type(grade))
		updateRuolo(xid[0],grade) #idUtente / Ruolo
		msg.page.redirect = '/backend/gestioneUtente/'