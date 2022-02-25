#todos/helper.py

#Metodi generici per le funzioni del views (Controller)

import asyncio
import time
import os
from os import listdir
from os.path import isfile, join
import glob

lista = {}

#Funzione per creazione del dizionario degli agenti inviato nella sessione
def createListaAgenti(path):
	#print('createListaAgenti')
	searching = path + '*.py'
	fileAgente = [os.path.basename(x) for x in glob.glob(searching)]

	dizionario = {}
	for nome in fileAgente:
		#Nome = Colore, stato, filtro
		dizionario[nome] = ['#444444', 1, 1]
	#print('Dizionario ', dizionario)

	return dizionario

async def riempiLista():
	print('riempiLista()')
	lista['02'] = 'miao'
	lista['3'] = 'miao'
	lista['11'] = 'miao'
	lista['099'] = 'miao'


async def getLista():
	print('getLista --' , lista)



	return lista