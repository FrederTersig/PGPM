#!/usr/bin/python
# This Python file uses the following encoding: utf-8
'''
@author: Federico Tersigni
'''

import justpy as jp



s = {} #Sessione


def esisteSessione(s_id):
	if s_id in s:
		return True
	else:
		return False

def utenteLoggato(s_id):
	return s[s_id]['logged_in']

def returnSessione(s_id):
	return s[s_id]

def cancellaSessione(s_id):
	print('Cancella Sessione')
	s[s_id]={}
	s[s_id]['logged_in'] = False


def returnElemento(s_id,chiave):
	return s[s_id][chiave]

def creaSessione(s_id, logged):
	print('********************* CREO SESSIONE')
	#if not esisteSessione(s_id):
	#	print('NON ESISTE SESSIONE')
	s[s_id]={}
	s[s_id]['logged_in'] = logged
	#else:
	#	print('ESISTE SESSIONE!')


def addElementoSessione(s_id, chiave, elemento):
	print('###########################')
	print('Aggiungo Elemento a sessione')
	if esisteSessione(s_id):
		s[s_id][chiave] = elemento
		print('Aggiunto')
	else:
		print('Non Aggiunto')
	print('###########################')

def addAgenteInSessione(s_id,agente,elemento):
	print('####')
	print('aggiungo agente a sessione')
	if esisteChiave(s_id,'agenti'):
		print('procedo')
		s[s_id]['agenti'][agente] = elemento
	else:
		print('NON esiste chiave')

def cambiaAttributoAgente(s_id,chiave, agente, indice, elemento):
	print('######')
	print('cambio attributo agente elemento')
	if esisteChiave(s_id, chiave):
		print('procedo')
		#print(type(s[s_id][chiave][agente]))
		print('PRIMA === ', s[s_id][chiave][agente])
		s[s_id][chiave][agente][indice] = elemento
		#print(s[s_id][chiave][agente][indice])
		print('DOPO === ', s[s_id][chiave][agente])
		#print(s[s_id][chiave])
		#print(s[s_id][chiave][chiaveAgente])
		#s[s_id][chiave][chiaveAgente][indice] = elemento
	else:
		print('non esiste chiave')

def cambiaAttributo(s_id,chiave,indice,elemento):
	print('cambia attributo')
	if esisteChiave(s_id,chiave):
		print('procedo')
		xUtente = list(s[s_id][chiave])
		xUtente[indice]=elemento
		xUtenteSet = tuple(xUtente)
		s[s_id][chiave] = xUtenteSet

		print('Riuscito')
	else:
		print('non esiste chiave')

def eliminaAgente(s_id,chiave, agente):
	if esisteChiave(s_id, chiave):
		print('PRIMA === ', s[s_id][chiave])
		del s[s_id][chiave][agente]
		print('DOPO === ', s[s_id][chiave])
	else:
		print('non sono riuscito')
def esisteChiave(s_id, chiave):
	if chiave in s[s_id]:
		return True
	else:
		return False

def showSessione(s_id):
	print('showSessione')
	#print('Mostro Sessione::: ' , s[s_id])