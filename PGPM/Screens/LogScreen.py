#!/usr/bin/python
# This Python file uses the following encoding: utf-8
'''
@author: Federico Tersigni
'''


#from Engine.Agente import Agente

from Template.LogView import LogView
from Template.LogView import addLog
from Template.LogView import insertButton


import sys
import os
import shutil
import signal
sys.path.append('../')
from Handler.AgentHandler import agentThread
from Handler.AgentHandler import getPathTempo
from Handler.AgentHandler import getTempo
#from Handler.AgentHandler import creaLog
#from Handler.AgentHandler import inserisciLog
import asyncio


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

import justpy as jp
import time
import queue
import threading

import subprocess
import logging


#Costanti delle Classi / Tailwind dei bottoni
agentiClasses = 'inline-block rounded w-32 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
agentiOnMouseOver = 'inline-block rounded w-32 h-16 bg-blue-600 m-2 text-white hover:bg-blue-400 focus:outline-white hover:text-white container'
buttonClasses = 'block rounded w-16 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
acceptClasses = 'block rounded w-16 h-16 m-2 bg-green-600 text-white hover:bg-green-300 focus:outline-white hover:text-gray-800'
rejectClasses = 'block rounded w-16 h-16 m-2 bg-red-600 text-white hover:bg-red-300 focus:outline-white hover:text-gray-800'
actionButtonClasses = 'block rounded w-32 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
#Codice della grafica della schermata di LOG

#Output cercato dalla schermata di log (Usare chiamata con API)
#Variabili output: per ora solo prove


############################################
processes=[]
threads = []
mutex = threading.Lock()
#session = {}
#agenti = {}
#path = ''

class LogScreen:

	play = True
	

	async def logScreen(self,request):
		print('LOGSCREEN')
		 # Procedura di Sessione
		s_id = request.session_id
		if not esisteSessione(s_id):
			creaSessione(s_id,False)
		else:
			#METTI TUTTI I DATI NELLE VARIABILI CHE MI SERVONO
			#IF PER VEDERE SE SIAMO LOGGATI O MENO
			if utenteLoggato(s_id):
				session = returnSessione(s_id)
			else:
				print('redirect da fare')

		#Il log può essere raggiunto SOLO se è stato cliccato 'run' nella startView

		if 'agenti' in session and 'path' in session:
			#Ci sono agenti instanziati nella sessione
			agenti = returnElemento(s_id,'agenti')
			path = returnElemento(s_id,'path')
		else:
			print('redirect da fare!')


		wp = LogView(session,self.showLog,self.stop)
		return wp

	#Funzione che crea i log, che scrive sulla gui
	async def showLog(self,msg):
		inizioIn = time.time()
		print('logscreen showlog')
		s_id = msg.session_id
		session = returnSessione(s_id)
		if 'agenti' in session and 'path' in session:
			#Ci sono agenti instanziati nella sessione
			agenti = returnElemento(s_id,'agenti')
			path = returnElemento(s_id,'path')
		else:
			print('redirect da fare!')

		#agenti = ['voce.py','voceb.py'] # lista nomi agente (attributo UNIVOCO dell'agente)
		xQueue = queue.Queue()
		test_time= time.time() + 20 # 5 secondi
		#agPath = '/home/federico/Scrivania/Handler/'
		
		pathTempo = getPathTempo()
		#print(pathTempo)
		xPath = 'run/LOG'+pathTempo+'.log'
		#print(xPath)
		filepath = path + xPath

		pathExist = os.path.exists(path+'run/')
		if not pathExist:
			os.mkdir(path+'run/')

		logging.basicConfig(filename=filepath, encoding='utf-8',level=logging.INFO,force=True)
		

		
		logging.info(getTempo() + ' -> Apertura del programma')
		
		addLog(msg.page.logFrameDiv, getTempo() + ' -> Apertura del programma', 'alert')
		
		await msg.page.update()

		print('CREO PROCESSI')
		for agent in agenti:
			#print('per ogni agente in agenti')
			if agenti[agent][1] == 1:
				x = subprocess.Popen(['python3 -u '+path+agent],shell=True,universal_newlines=True, bufsize=100 ,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
				processes.append(x)
				thread = agentThread(agent,x.stdout,xQueue,agenti[agent][0])
				initLog = getTempo() + ' -> Inizializzazione thread: ' + agent
				logging.info(initLog)
				#addLog(msg.page.logFrameDiv, initLog, 'alert')
				
				thread.daemon=True
				threads.append(thread)

		addLog(msg.page.logFrameDiv, getTempo() + ' -> Ho inizializzato tutti i Thread','alert')
		await msg.page.update()
		for t in threads:
			#print('partono i thread')
			t.start()
			startLog = getTempo() + ' -> Partenza esecuzione thread: ' + t.getNome()
			logging.info(startLog)
			#addLog(msg.page.logFrameDiv, startLog, thread.getColore())
		addLog(msg.page.logFrameDiv, getTempo() + ' -> Ho fatto partire tutti i Thread','alert')
		await msg.page.update()
		fineIn = time.time()
		#RISULTATO
		risultatoIn = fineIn - inizioIn
		print('##############################################################################')
		print('NOTA: Tempo espresso in Secondi.')
		print('Tempo passato per il caricamento e la partenza dei thread: ', risultatoIn)
		print('##############################################################################')
		try:
			while True:
				if not self.play:
					
					logging.warning('Programma stoppato')
					addLog(msg.page.logFrameDiv, 'Programma stoppato','alert')
					addLog(msg.page.logFrameDiv, '### ATTENZIONE :: Aspettare che il programma sia stoppato ###','alert')
					await msg.page.update()
					break
				for p in processes:
					p.poll()


				if not xQueue.empty():
					data = xQueue.get(False)
					xQueue.task_done()
					chiaveAgente=data.split('|')[0]
					coloreAgente=agenti[chiaveAgente][0]
					logText = data.split('|')[1]
					#print('#################')
					#addLog(msg.page.logFrameDiv,logText+'\n', coloreAgente)
					#await msg.page.update()
					#Scrivi sul log
					logging.info(logText)
				await msg.page.update()
				
				
		except Exception as e:
			print('ECCEZIONE!!', e)
		inizio = time.time()
		for p in processes:
			if p.poll() is None:
				#p.terminate()
				os.kill(p.pid, signal.SIGTERM)
		print('MI FERMO PRIMA DI T IN THREADS')
		addLog(msg.page.logFrameDiv, getTempo()+ ' -> Inizio la chiusura dei Thread', 'alert')
		await msg.page.update()
		for t in threads:
			t.stopFunc()
			name = t.getNome()
			chiusuraLog = getTempo() + ' -> Chiusura del thread in corso: ' + thread.getNome()
			#print(name, '=', t.is_alive())
			logging.info(chiusuraLog)
			#addLog(msg.page.logFrameDiv, chiusuraLog, 'alert')
			#await msg.page.update()
			t.join()

			terminazioneLog = getTempo() + ' -> Thread terminato: ' + thread.getNome()
			logging.info(terminazioneLog)
			#addLog(msg.page.logFrameDiv, terminazioneLog, 'alert')
			#await msg.page.update()
		
		
		threads.clear()
		processes.clear()
		self.play=True
		addLog(msg.page.logFrameDiv, getTempo()+ ' -> Ho chiuso tutti i Thread', 'alert')
		logging.info('Esecuzione Conclusa')
		addLog(msg.page.logFrameDiv, 'Esecuzione Conclusa - Si può uscire', 'alert')
		
		#FINISCE TEMPO
		fine = time.time()
		#RISULTATO
		
		risultatoFinale = fine - inizio
		print('##############################################################################')
		print('NOTA: Tempo espresso in Secondi.')
		print('Tempo passato dalla richiesta di terminazione dei processi: ', risultatoFinale)
		print('##############################################################################')

		insertButton(msg.page.subNavDiv)
		await msg.page.update()

	#Definizione in cui usare un segnale per bloccare il while
	async def stop(self,msg):
		print('fermo gli agenti')
		self.play = False
