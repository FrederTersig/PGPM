#!/usr/bin/python
# This Python file uses the following encoding: utf-8
'''
@author: Federico Tersigni
'''

import os
import sys
from os import listdir
from os.path import isfile,join
import glob


import justpy as jp
import sys



from Template.FilterView import FilterView
from Template.FilterView import ShowRimuovi
from Template.FilterView import ShowAggiungi
from Template.FilterView import ShowMenuFiltroAgente
from Template.FilterView import ShowButtonFiltroAgente

from Screens.Sessione import esisteSessione
from Screens.Sessione import creaSessione
from Screens.Sessione import showSessione
from Screens.Sessione import utenteLoggato
from Screens.Sessione import returnSessione
from Screens.Sessione import esisteChiave
from Screens.Sessione import returnElemento
from Screens.Sessione import addElementoSessione
from Screens.Sessione import cambiaAttributoAgente


#Costanti delle Classi / Tailwind dei bottoni
agentiClasses = 'inline-block rounded w-32 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
agentiOnMouseOver = 'inline-block rounded w-32 h-16 bg-blue-600 m-2 text-white hover:bg-blue-400 focus:outline-white hover:text-white container'


buttonClasses = 'block rounded w-16 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
acceptClasses = 'block rounded w-16 h-16 m-2 bg-green-600 text-white hover:bg-green-300 focus:outline-white hover:text-gray-800'
rejectClasses = 'block rounded w-16 h-16 m-2 bg-red-600 text-white hover:bg-red-300 focus:outline-white hover:text-gray-800'
actionButtonClasses = 'block rounded w-32 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'

#Codice della grafica della schermata di LOG
############################################
#Prima di tutto, creo un'istanza della classe Agente


#session = {}

class FilterScreen:
	async def filterScreen(self,request):
		print('FILTERSCREEN')
		#listaAgenti = h.getListaAgenti()

		 # Procedura di Sessione
		s_id = request.session_id
		if not esisteSessione(s_id):
			creaSessione(s_id,False)
		else:
			#METTI TUTTI I DATI NELLE VARIABILI CHE MI SERVONO
			#IF PER VEDERE SE SIAMO LOGGATI O MENO
			showSessione(s_id)

		print('check per gli agenti')
		
		session = returnSessione(s_id)


		wp = FilterView(self.filtroAgEntra, self.filtroAgEsce,session)
		return wp
	
	#Lista di Eventi
	def onClickRimuovi(self,msg):
		print('ONCLICKRIMUOVI ')
		s_id = msg.session_id
		print('?')
		self.setFiltroAgente(s_id,msg.target.chiave,0)
		print('SETTO FILTRO = FALSE')
		ShowAggiungi(msg.target, self.onClickAggiungi)
		print('FINE ONCLICKRIMUOVI ')

	def onClickAggiungi(self,msg):
		print('ONCLICKAGGIUNGI')
		s_id = msg.session_id
		self.setFiltroAgente(s_id,msg.target.chiave,1)
		print('SETTO FILTRO = TRUE')
		ShowRimuovi(msg.target, self.onClickRimuovi)
		print('FINE ONCLICKAGGIUNGI')


	def filtroAgEntra(self,msg):
		print('entra in filtro')
		#Manca elemento per il filtro
		#filtro = self.getFiltroAgente(msg.target.chiave)
		s_id = msg.session_id
		listaAgenti = {}
		if esisteChiave(s_id, 'agenti'):
			print('esistono agenti in sessione')
			listaAgenti = returnElemento(s_id, 'agenti')

		ShowMenuFiltroAgente(msg.target, listaAgenti, self.onIcona, self.leaveIcona, self.onClickRimuovi, self.onClickAggiungi, self.cambioColore)


	def cambioColore(self,msg):
		print('provo a cambiare colore: ')
		s_id =msg.session_id
		#print('check settaggio colore', msg.target.value)
		# Chiave - msg.target.chiave
		# Colore - msg.target.value
		#h.setColoreAgente(msg.target.chiave, msg.target.value)
		#showSessione(s_id)
		print('voglio mettere questo colore- ', msg.target.value)
		cambiaAttributoAgente(s_id,'agenti',msg.target.chiave,0,msg.target.value)
		#showSessione(s_id)

		print('Fine cambio colore')


	def filtroAgEsce(self,msg):
		
		print('esce dal bottone')
		ShowButtonFiltroAgente(msg.target, self.filtroAgEntra, self.filtroAgEsce)
		print('fine')

	#def showAgentButtons(self):
	#    print('prova')
	
	def onIcona(self, msg):
		print('tocco icona')
		msg.target.fill='red'
		#print(msg.target.components[0].d)

	def leaveIcona(self,msg):
		print('esco icona')
		msg.target.fill='currentColor'


	def setFiltroAgente(self,s_id,chiave, value):
		print('setFiltroAgente in HandlerAgente')
		pro = returnSessione(s_id)
		print('PRIMA_-------------------------------------')
		print(pro)
		cambiaAttributoAgente(s_id,'agenti',chiave, 2, value)
		pro = returnSessione(s_id)
		print('DOPO_--------------------------------------')
		print(pro)

		print('settato il filtro')

	def getFiltroAgente(self,chiave):
		listaAgenti = h.getListaAgenti()
		return listaAgenti[chiave][2]


