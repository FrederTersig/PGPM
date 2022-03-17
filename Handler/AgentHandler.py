import time
import subprocess
import threading
import sys
import queue
import asyncio

#importo il logging
#import logging
from datetime import datetime
#from Template.LogView import addLog




# Classe Thread Personalizzata
class agentThread(threading.Thread):
	def __init__(self,nome, out, queue, colore):
		threading.Thread.__init__(self)
		self.nome = nome
		self.pipe = out
		self.queue = queue
		self.stop = False
		self.colore = colore


	def getNome(self):
		return self.nome

	#Funzione di stop
	def stopFunc(self):
		self.stop = True

	def getColore(self):
		return self.colore

	#Funzione di lettura dell'output
	def lettura(self):
		while not self.stop:
			#-- UNO ALLA VOLTA

			#print(' NOME DEL THREAD CHE HA IL MUTEX' + self.getNome())
			l=self.pipe.readline()
			if l != '':
				#data = self.getNome() + ' : ' + l

				self.queue.put(self.nome+'|'+getTempo() +'-Agente: '+self.nome+' = ' + l)

	#Modifica della funzione di run interna alla classe Thread
	def run(self):
		try:
			#threadLock.acquire()
			self.lettura()
			#threadLock.release()
		except Exception as e:
			print('Eccezione in run: ', e)

	#def join(self):
	#	threading.Thread.join(self)


def getPathTempo():
	tempo = datetime.now()
	tempoLog = tempo.strftime("%m-%d-%Y_%H-%M-%S")
	return tempoLog

def getTempo():
	tempo = datetime.now()
	tempoLog = tempo.strftime("%H:%M:%S")
	return tempoLog



#isNotExist = os.path.exists('/home/federico/Scrivania/Handler/run/prova.log')
#print(isNotExist)
#isExist = os.path.exists('/home/federico/Scrivania/Handler/run/')
#print(isExist)