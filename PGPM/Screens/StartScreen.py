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
from Model.DAO.RunDAO import insertRun
from Model.DAO.AgenteDAO import insertAgente
from Model.DAO.DirectoryDAO import insertDirectory


from Template.StartView import StartView
from Template.StartView import ShowMenuAgente
from Template.StartView import ShowPlay
from Template.StartView import ShowStop
from Template.StartView import ShowButtonAgente

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


#Costanti delle Classi / Tailwind dei bottoni
coloreAgente = 'background-color:'
agentiClasses = 'inline-block rounded w-32 h-16 m-2 bg-[#FFFFFF] text-white hover:bg-white focus:outline-white hover:text-gray-800'
agentiOnMouseOver = 'inline-block rounded w-32 h-16 bg-blue-600 m-2 text-white hover:bg-blue-400 focus:outline-white hover:text-white container'


buttonClasses = 'block rounded w-16 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
acceptClasses = 'block rounded w-16 h-16 m-2 bg-green-600 text-white hover:bg-green-300 focus:outline-white hover:text-gray-800'
rejectClasses = 'block rounded w-16 h-16 m-2 bg-red-600 text-white hover:bg-red-300 focus:outline-white hover:text-gray-800'
actionButtonClasses = 'block rounded w-32 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'

#Codice della grafica della schermata di LOG
############################################
#Prima di tutto, creo un'istanza della classe Agente



class StartScreen:
	#def __init__(self):
	#    pass
	#Codice della schermata di Start

	async def startScreen(self, request):
		s_id = request.session_id
		print('STARTSCREEN -')
		session = {}
		#print(request.cookies.get('jp_token'))
		
		# Procedura di Sessione
		if not esisteSessione(s_id):
			creaSessione(s_id,False)
		else:
			#METTI TUTTI I DATI NELLE VARIABILI CHE MI SERVONO
			#IF PER VEDERE SE SIAMO LOGGATI O MENO
			if utenteLoggato(s_id):
				session = returnSessione(s_id)
			

			#showSessione(s_id)

		print('Check per gli agenti')

		session = returnSessione(s_id)

		# Fine Procedura di Sessione
		wp = StartView(self.agEntra, self.agEsce, self.startRun,self.addAgente,session)
		

		return wp


	def addAgente(self,msg):
		print('Funzione Add Agente')
		s_id = msg.session_id
		nomeAgente = msg.form_data[0]['value']
		nomeAgente = nomeAgente + '.py'
		print('prima delle if ---', nomeAgente)
		if esisteSessione(s_id):
			session = returnSessione(s_id)
			print('ritorno Sessione')
			if 'path' in session and 'agenti' in session and 'utente' in session:
				print('Esiste la sessione con i vari attributi')
				#Nome dell'agente è UNICO
				if nomeAgente not in session['agenti']:
					print('procedo con creazione Agente')
					p = session['path']
					loc = p+nomeAgente
					print('prova-a')
					#SE non esistono le cartelle del path, creale
					basedir = os.path.dirname(loc)
					if not os.path.exists(basedir):
						os.makedirs(basedir)
					print('prova-b')
					#creo file vuoto
					open(loc,'a').close()
					#memorizzo sulla sessione
					print('prova-c')
					elemento = ['#444444', 1,1]
					addAgenteInSessione(s_id,nomeAgente,elemento)
				else:
					print('esiste nuovoNome in session-listaAgenti')
			else:
				print('non esiste listaAgenti O path nella sessione')
		else:
			print('non esiste sessione')

		msg.page.redirect = '/'


	def startRun(self,msg):
		print('Inizializzo la run')
		s_id = msg.session_id
		#print('?')
		if esisteSessione(s_id):
			#print('?')
			session = returnSessione(s_id)
			#'utemte'
			if session['logged_in'] and 'path' in session and 'nome_path' in session and 'agenti' in session and 'utente' in session:
				print('procedo nella insert generale')
				path = session['path']
				nomePath = session['nome_path']
				idUtente = session['utente'][0]
				#print('idUtente = ',idUtente)
				
				
				#print('idRun=', idRun)
				
				idDirectory = insertDirectory(idUtente,path,nomePath)
				idRun = insertRun(idUtente,idDirectory)
				#print('inserisco Directori in id: ', idRun)
				#print('idDirectory=', idDirectory)
				#print('prendo idDirectory ', idDirectory)
				for agente in session['agenti']:
					colore = session['agenti'][agente][0]
					stato = session['agenti'][agente][1]
					filtro = session['agenti'][agente][2]

					if stato == 1:

						insertAgente(agente, idDirectory, colore,stato,filtro)
				
				print('Fine Inserimento delle cose in sessione, Mostro la sessione')
				showSessione(s_id)
				#Vado al log Screen
				msg.page.redirect = '/log'

				
			else:
				print('Manca qualcosa per la insert')


		else:
			print('La sessione non esiste')



	# Eventi del mouse comuni per ogni icona ---------------------------------------------
	def onIcona(self, msg):
		print('tocco icona')
		msg.target.fill='red'

	def leaveIcona(self,msg):
		print('esco icona')
		msg.target.fill='currentColor'

	# Eventi click che richiama la funzione corrispondente -------------------------------
	def onClickCode(self,msg):
		print('Apre il codice sorgente dell agente selezionato')
		

	def onClickPlay(self, msg):
		print('Agente Attivato')
		#print(msg.target)
		self.setStatoAgente(msg.session_id,msg.target.chiave, 1)

		ShowStop(msg.target, self.onClickStop)
		print('fine onClickPlay')

	
	def onClickStop(self, msg):
		print('Agente Disattivato')
		#print(msg.target)
		self.setStatoAgente(msg.session_id,msg.target.chiave, 0)
		ShowPlay(msg.target, self.onClickPlay)

		print('fine onClickStop')

	#prova EVENTI -- Prova a inserire altri eventi negli elementi aggiunti da 'agEntra' per vedere la loro efficacia
	def agEntra(self,msg): 
		print('entro in agente')
		s_id = msg.session_id
		print('CHIAVE AGENTE = ', msg.target.chiave)
		listaAgenti = {}
		if esisteChiave(s_id, 'agenti'):
			print('esistono agenti in sessione')
			listaAgenti = returnElemento(s_id, 'agenti')

		#print('------', listaAgenti)
		ShowMenuAgente(msg.target, listaAgenti, self.onIcona, self.leaveIcona, self.onClickStop, self.onClickPlay, self.onDeleteAgente)

	########################
	def agEsce(self,msg):

		print('---- esco dal bottone di un agente')
		ShowButtonAgente(msg.target, self.agEntra, self.agEsce)

	def listaFileAgente(self):
		fnames = [os.path.basename(x) for x in glob.glob('dirAgenti/*.py')]

		#path = os.path.abspath('dirAgenti/')
		#mylist = [f for f in glob.glob('dirAgenti/*.py')]
		print(fnames)
		print('listaAgenti -------')
		return fnames

	def setStatoAgente(self,s_id,chiave,value):
		print('SETTA STATO AGENTE')
		cambiaAttributoAgente(s_id,'agenti',chiave, 1, value)
		print('------------------')


	def onDeleteAgente(self,msg):
		print('sto cancellando agente')
		s_id = msg.session_id
		pos=''
		chiave = msg.target.chiave
		print(chiave, 'IN MEZZO ONDELETE')
		if esisteChiave(s_id,'path'):
			print('ESISTE CHIAVE??')
			s = returnSessione(s_id)
			location = s['path']
			print(location)
			pos = os.path.join(location,chiave)
			print(pos)
			os.remove(pos)
			eliminaAgente(s_id,'agenti',chiave)
		print('FINE ONDELETEAGENTE')
		msg.page.redirect = '/'


		


	
