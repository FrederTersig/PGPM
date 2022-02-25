#todos/views.py

import sys
import os
import time
import asyncio
from django.shortcuts import redirect,render
from django.template import Context

#sys.path.append('../')
#from Engine.HandlerAgente import HandlerAgente

from todos.helper import createListaAgenti
from todos.helper import riempiLista
from todos.helper import getLista
from todos.agentHandler import agentThread
from todos.agentHandler import getPathTempo
from todos.agentHandler import getTempo

from todos.models import Utente
from todos.models import Agente
from todos.models import Directory
from todos.models import Run

from django.core.exceptions import ObjectDoesNotExist

###
import subprocess
import threading

import queue

#importo il logging
import logging
from datetime import datetime

###

stopBool = False
processes = []
threads = []
output=[]
xQueue = queue.Queue()


def startScreen(request):
	listaAgenti={} #Lista Agenti
	ruolo=0
	email=''
	logged=False
	path=''
	print('PROVA DEL CODICE DI VIEWS')

	if request.session.has_key('email'):
		print('sono loggato nel sistema')
		email = request.session['email']
		ruolo = request.session['ruolo']
		logged = True
	
	if request.session.has_key('path') and request.session.has_key('listaAgenti'):
		#path = request.session['path']
		listaAgenti = request.session['listaAgenti']


	#print(listaAgenti.get('Agente_002'))

	#x = Utente(nome='Gianlupo', email='Gianlupo@gmail.com',password='password',ruolo=1)
	#x.save()
	#print(x)
	return render(request, 'startScreen.html',{'listaAgenti' : listaAgenti,'email':email ,'ruolo' : ruolo, 'logged':logged})

##################################
#Codice della schermata di Log-###

def logScreen(request):
	print('logScreen')
	global stopBool
	stopBool = False
	ruolo=0
	email=''
	logged=False
	output.clear()
	print('PROVA DEL CODICE DI VIEWS')
	if request.session.has_key('email') and request.session.has_key('path') and request.session.has_key('listaAgenti'):
		print('sono loggato nel sistema')
		email = request.session['email']
		ruolo = request.session['ruolo']
		path = request.session['path']
		agenti = request.session['listaAgenti']
		logged = True
	else:
		return redirect('startScreen')

	str_tempo = getPathTempo()
	pathRun ='run/LOG'+str_tempo+'.log'

	filePath = path + pathRun
	pExists = os.path.exists(path+'run/')
	if not pExists:
		os.mkdir(path+'run/')
	logging.basicConfig(filename=filePath, encoding='utf-8',level=logging.INFO,force=True)

	
	#test_time = time.time()+5

	output.append([getTempo()+ ' -> Apertura del programma','alert'])
	logging.info(getTempo()+ ' -> Apertura del programma')
	for agent in agenti:
		#SE lo stato dell'agente è 1
		if agenti[agent][1] == 1:
			x = subprocess.Popen(['python3 -u '+path+agent],shell=True,universal_newlines=True, bufsize=100 ,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
			processes.append(x)
			#agCol = agenti[agent][0]
			thread = agentThread(agent,x.stdout,xQueue,agenti[agent][0])
			output.append([getTempo() + ' -> Inizializzazione thread: ' + agent,agenti[agent][0]])
			logging.info(getTempo() + ' -> Inizializzazione thread: ' + agent)
			thread.daemon=True
			threads.append(thread)

	for thread in threads:
		#_stringa = 'Eseguo il thread per agente: '+ thread.getNome()
		thread.start()
		#print('Thread appena creato: ', thread.is_alive())
		output.append([getTempo() + ' -> Partenza esecuzione thread: ' + thread.getNome(),thread.getColore()])
		logging.info(getTempo() + ' -> Partenza esecuzione thread: ' + thread.getNome())





	####################
	return render(request, 'logScreen.html',{'email':email ,'ruolo' : ruolo, 'logged':logged, 'listaLog':output})


async def showLog(request):
	print('showLog - Update del frame dei LOG ')


	if not stopBool:
		print('aggiorno')
		#Provo ad aggiornare continuamente qualcosa
		for p in processes:
			p.poll()

		if not xQueue.empty():
			data = xQueue.get(False) # Rimuovo oggetto dalla coda
			xQueue.task_done()
			coloreAgente=data.split('|')[0]
			#coloreAgente=agenti[chiaveAgente][0]

			output.append([data,coloreAgente])
			logging.info(data)
			print(data+'\n', ' ========= ', stopBool)

	return render(request, 'updateLog.html',{'listaLog':output})


async def stopLog(request):
	global stopBool
	stopBool = True
	print('stopLog - Ferma esecuzione dei thread', stopBool)
	print('################################################')
	output.append(['Programma Stoppato','alert'])
	logging.info('Programma Stoppato')
	for t in threads:
		print('fermo un thread')
		t.stopFunc()
		name = t.getNome()
		chiusuraLog = getTempo() + ' -> Chiusura del thread in corso: ' + t.getNome()
		output.append([chiusuraLog,'alert'])
		logging.info(chiusuraLog)
		t.join()
		terminazioneLog = getTempo() + ' -> Thread terminato: ' + t.getNome()
		output.append([terminazioneLog,'alert'])
		logging.info(terminazioneLog)
		print('riuscito a fermare un thread')
	threads.clear()
	processes.clear()
	output.append(['Esecuzione Conclusa','alert'])
	logging.info('Esecuzione Conclusa')
	print('ho finito tutto')
	return render(request,'stopLog.html',{'listaLog':output})

#Fine codice della schermata di Log-###
#######################################
def filterScreen(request):
	print('filterScreen')
	listaAgenti={}
	nLista={}
	ruolo=0
	email=''
	logged=False
	print('PROVA DEL CODICE DI VIEWS')
	if request.session.has_key('email'):
		print('sono loggato nel sistema')
		email = request.session['email']
		ruolo = request.session['ruolo']
		logged = True

	if request.session.has_key('path') and request.session.has_key('listaAgenti'):
		#path = request.session['path']
		listaAgenti = request.session['listaAgenti']

	for ag in listaAgenti:
		newNome = ag[:-3]
		nLista[newNome]=listaAgenti[ag]

	#nome = elemento[0][:-3]
	print(nLista)
	return render(request, 'filterScreen.html',{'listaAgenti' : nLista,'email':email ,'ruolo' : ruolo, 'logged':logged})

def configScreen(request):
	print('configScreen')
	logged = False
	email = ''
	ruolo = 0
	listaRun={}
	listaDirectory={}
	if request.session.has_key('email'):
		print('sono loggato nel sistema')
		email = request.session['email']
		ruolo = request.session['ruolo']
		ID = request.session['id']
		logged = True

		qRun = Run.objects.filter(utente_id=ID)
		#print('Mostro query run', qRun)
		for x in qRun:
			
			listaRun[x.id]=x.timestamp
			y = Directory.objects.get(run_id_id=x.id)
			listaDirectory[y.id]=[y.path,y.run_id_id]

		
		#qPath = Directory.objects.filter()
		#queryPath = Directory.objects.raw(f'SELECT todos_directory.path from todos_directory, todos_run, todos_utente where todos_directory.run_id_id = todos_run.id AND todos_run.utente_id_id = 2;')
		#for x in queryPath:
		#	print(x)
		#print(queryPath.id)
		#Due Query:
		#1) per i path che hai usato in precedenza
		#2) per le run che ha fatto e che può decidere di cancellare
	return render(request,'configScreen.html',{"email":email, "ruolo":ruolo, "logged":logged, "listaRun":listaRun, "listaDirectory":listaDirectory})


def backendScreen(request):
	print('backend')

	if not request.session.has_key('email'):
		redirect('startScreen')

	return render(request, 'backendScreen.html')

#Schermate backend --- 


#try:
#	x = Utente.objects.get(nome='Gianlupo')

		#print('-----------------------------------')
		#print(' ?????? ', type(x))
		#print(x.nome, x.password, x.email)
#except ObjectDoesNotExist:

def backendUtenteScreen(request):
	print('backend Utente')
	listaUtenti = {}
	if not request.session.has_key('email'):
		redirect('startScreen')
	try:
		queryUtenti = Utente.objects.all()
		#print(listaUtenti)
		for u in queryUtenti:
			listaUtenti[u.email]=[u.id,u.nome,u.password,u.ruolo]

	except ObjectDoesNotExist:
		print('eccezione')
	print(listaUtenti)
	print(type(listaUtenti))

	return render(request, 'backendUtenteScreen.html', {'listaUtenti':listaUtenti})

def cancellaUtente(request,ID):
	print('Cancella un utente')
	print(ID)
	print('----')
	try:
		Utente.objects.get(id=ID).delete()
		

	except ObjectDoesNotExist:
		print('Eccezione')

	return redirect('backendUtenteScreen')

def backendRunScreen(request):
	print('backend Run')
	
	if not request.session.has_key('email'):
		redirect('startScreen')
	listaRun={}
	try:
		queryRun = Run.objects.all()
		for u in queryRun:
			listaRun[u.id]=[u.timestamp, u.utente_id_id]
	except ObjectDoesNotExist:
		print('eccezione')



	return render(request, 'backendRunScreen.html', {'listaRun':listaRun})

def cancellaRun(request,ID):
	print('Cancella un run')
	print(ID)
	print('----')
	try:
		Run.objects.get(id=ID).delete()
	except ObjectDoesNotExist:
		print('Eccezione')

	return redirect('backendRunScreen')

def backendDirectoryScreen(request):
	print('backend directory')
	if not request.session.has_key('email'):
		redirect('startScreen')
	listaDirectory={}
	try:
		queryDirectory = Directory.objects.all()
		for u in queryDirectory:
			listaDirectory[u.id]=[u.nome, u.path, u.run_id_id]
	except ObjectDoesNotExist:
		print('eccezione')

	return render(request, 'backendDirectoryScreen.html', {'listaDirectory':listaDirectory})

def cancellaDirectory(request,ID):
	print('Cancella una Directory')
	print(ID)
	print('----')
	try:
		Directory.objects.get(id=ID).delete()
	except ObjectDoesNotExist:
		print('Eccezione')

	return redirect('backendDirectoryScreen')

def backendAgenteScreen(request):
	print('backend Agente')
	listaAgenti= {}
	if not request.session.has_key('email'):
		redirect('startScreen')
	try:
		queryAgenti = Agente.objects.all()
		#print(listaUtenti)
		for u in queryAgenti:
			listaAgenti[u.nome]=[u.id,u.colore,u.filtro,u.directory_id_id,u.stato]

	except ObjectDoesNotExist:
		print('eccezione')

	print(listaAgenti)
	return render(request, 'backendAgenteScreen.html', {'listaAgenti':listaAgenti})
	

def cancellaAgenteDB(request,ID):
	print('Cancella una Directory')
	print(ID)
	print('----')
	try:
		Agente.objects.get(id=ID).delete()
	except ObjectDoesNotExist:
		print('Eccezione')

	return redirect('backendAgenteScreen')

#Fine schermate backend ---


#inizio codice animazioni bottoni startScreen#################################################

def setStato(request):
	print('setStato : request')

	elemento = list(request.POST.lists())[0]
	print('#################################')
	print(elemento)
	nome = elemento[0]
	colore = elemento[1][0]
	stato = int(elemento[1][1])
	filtro = int(elemento[1][2])
	print(stato, '<---- stato')
	if stato == 1:
		#print('stato è 1')
		stato=0
	else:
		#print('stato non è 1')
		stato=1
		
	request.session['listaAgenti'][nome][1]=stato
	request.session.save()
	#print('Fine request setStato ###', request.session['listaAgenti'][nome][1])

	return render(request, 'buttonAgente.html', {'nome' : nome, 'stato':stato, 'colore':colore, 'filtro':filtro})

#il bottone viene 'cambiato' quando il mouse si avvicina
def buttonAgente(request):
	#Ho bisogno dell'informazione dell'agente specifico per poter vedere se è in play o meno.
	print('buttonAgente : request --> ', request.GET)

	elemento =list(request.GET.lists())[0]
	nome = elemento[0]
	colore = elemento[1][0]
	stato = int(elemento[1][1])
	filtro = int(elemento[1][2])

	print('Fine request buttonAgente ##### ', nome, ' ', stato, ' ', colore, ' ', filtro)

	return render(request, 'buttonAgente.html', {'nome' : nome, 'stato':stato, 'colore':colore, 'filtro':filtro})

#il bottone viene 'ri-cambiato' quando il mouse esce 
def buttonAgenteBack(request):
	#listaAgenti=checkAgents()

	print('buttonAgenteBack : request --> ', request.GET)
	elemento =list(request.GET.lists())[0]
	nome = elemento[0]
	colore = elemento[1][0]
	stato = int(elemento[1][1])
	filtro = int(elemento[1][2])

	print('Fine request buttonAgenteBack ##### ', nome, ' ', stato, ' ', colore, ' ', filtro)

	return render(request, 'buttonAgenteBack.html', {'nome' : nome, 'stato':stato, 'colore':colore, 'filtro':filtro})

def deleteAgente(request):
	print('cancello un agente')
	nomeAgente = list(request.POST.lists())[0][0]
	#print(nomeAgente)
	location = request.session['path']
	path = os.path.join(location,nomeAgente)
	os.remove(path)
	del request.session['listaAgenti'][nomeAgente]
	request.session.save()
	return redirect('startScreen')

def startRun(request):
	print('inizializzo la run')
	#Faccio una insert della run. Gli agenti che verranno salvati
	#saranno solo quelli che avranno attivo=1
	#I dati da inserire sono TUTTI salvati nella sessione

	#1) Salvo Run con utente_id = utente.id attuale
	#2) Salvo Directory usando il path e id Run
	#3) Salvo Agente usando l'id della directory E stato==1

	if not request.session.has_key('id') or not request.session.has_key('path') or not request.session.has_key('listaAgenti'):
		redirect('startScreen')

	utente_id = request.session['id']
	path = request.session['path']
	listaAgenti = request.session['listaAgenti']

	nuovaRun = Run(timestamp='CURRENT TIMESTAMP', utente_id_id=utente_id)
	nuovaRun.save()

	nuovaDirectory = Directory(nome='prova', path=path, run_id_id=nuovaRun.id)
	nuovaDirectory.save()

	for x in listaAgenti:
	
		nuovoAgente = Agente(nome=x, colore=listaAgenti[x][0], stato=listaAgenti[x][1], filtro=listaAgenti[x][2], directory_id_id=nuovaDirectory.id)
		nuovoAgente.save()
	print('finito?')

	return redirect('logScreen')


def editorScreen(request,nomeAgente):
	print('editAgenteCode')
	print('nomeAgente = ',nomeAgente)
	if not request.session.has_key('email') or not request.session.has_key('path'):
		redirect('startScreen')
	path = request.session['path']

	codice = ''

	path = path+nomeAgente
	print(path)
	aPath = os.path.abspath(path)
	print('mostro cosa apro')
	with open(aPath,'r') as l:
		Linee = l.readlines()
			
		print(Linee)
		#print('#####', Linee[0])
		for n in Linee:
			codice = f'{codice}{n}'
			#print(codice)
		print('#', codice)
	l.close()
	#Codice è il corpo dell'agente specifico aperto in EditAgente
	#L'ultima cosa che resta è inserirlo nel dizionario del render

	print('QUESTO è CODICE:::')
	print(codice)
	return render(request,'editorScreen.html',{'nomeAgente' : nomeAgente, 'codice':codice})

def salvaCodice(request,nomeAgente):
	print('salvaCodice')
	codice = request.POST['testoAgente']
	print(codice)
	result=''
	#Prendi path assoluto dalla sessione
	#Aggiungi il nome.py a questo path
	p = request.session['path']
	pathCompleto = p+nomeAgente

	print(codice.splitlines())
	print('CODICE SALVATO GIUSTO?')
	print(result)
	path = os.path.abspath(pathCompleto)
	file_agente=open(path,'w')
	file_agente.write(codice)
	file_agente.close()

	return redirect('startScreen')

def addAgente(request):
	print('aggiungi Agente')
	nuovoNome=request.POST['nuovoAgente']
	nuovoNome=nuovoNome+'.py'
	if request.session.has_key('listaAgenti') and request.session.has_key('path'):
		if nuovoNome not in request.session['listaAgenti']:
			#Il nome non è presente nella sessione.
			p =  request.session['path']
			loc = p+nuovoNome
			print('prova-a')
			#SE non esistono le cartelle del path, le crei
			basedir = os.path.dirname(loc)
			if not os.path.exists(basedir):
				os.makedirs(basedir)
			print('prova-b')
			#crei un file vuoto con il nome dato dall'utente
			open(loc,'a').close()
			#memorizzo sulla sessione
			print('prova-c')
			request.session['listaAgenti'][nuovoNome]=['#444444', 1, 1]
			request.session.save()
			print('fine prova')
		else:
			print('esiste nuovoNome in session-listaAgenti')
	else:
		print('non esiste listaAgenti O path nella sessione')


	#Controlla che il nome sia UNICO nella sessione
	#Inserisci l'agente nella sessione con roba di default
	#Crea il file all'interno del path messo nella sessione
	return redirect('startScreen')

#Fine codice animazioni bottoni startScreen########################################################

#Inizio codice animazioni bottoni FILTERSCREEN######



def filtroButtonAgente(request):
	print('filtroButtonAgente ')

	elemento =list(request.GET.lists())[0]
	nome = elemento[0]
	
	colore = elemento[1][0]
	stato = int(elemento[1][1])
	filtro = int(elemento[1][2])

	print('Fine request filtroButtonAgente ##### ', nome, ' ', stato, ' ', colore, ' ', filtro)

	return render(request, 'filtroButtonAgente.html', {'nome' : nome, 'colore':colore,'stato':stato, 'filtro':filtro})

def filtroButtonAgenteBack(request):
	print('filtroButtonAgenteBack : request --> ', request.GET)

	elemento =list(request.GET.lists())[0]
	nome = elemento[0]
	
	colore = elemento[1][0]
	stato = int(elemento[1][1])
	filtro = int(elemento[1][2])

	print('Fine request filtroButtonAgenteBACK!!! ##### ', nome, ' ', stato, ' ', colore, ' ', filtro)

	return render(request, 'filtroButtonAgenteBack.html', {'nome' : nome, 'colore':colore,'stato':stato, 'filtro':filtro})



def editColor(request):
	print('#################################### Cambio del colore')
	elemento =list(request.POST.lists())[1]
	nome = elemento[0]
	ch = nome+'.py'
	colore = request.POST.get('nuovoColore')
	stato = int(elemento[1][1])
	filtro = int(elemento[1][2])
	#print('mostro la sessione')
	#print(request.session['listaAgenti'][nome])
	#print('colore? cambiato?')
	request.session['listaAgenti'][ch][0]=colore
	request.session.save()

	print('editColor - #### ', nome, ' ', stato, ' ', colore, ' ', filtro)
	return render(request, 'filtroButtonAgenteBack.html', {'nome' : nome, 'colore':colore, 'stato':stato, 'filtro':filtro})

def setFilter(request):
	print('#################################### Cambio della booleana filtro')
	elemento =list(request.POST.lists())[0]
	print('ELEMENTO --', elemento)
	nome = elemento[0]
	ch = nome+'.py'
	colore = elemento[1][0]
	stato = int(elemento[1][1])
	filtro = int(elemento[1][2])
	print('Filtro --- ', filtro)
	if filtro == 1:
		filtro = 0
	else:
		filtro = 1
	print('Filtro --- ', filtro)
	request.session['listaAgenti'][ch][2]=filtro
	request.session.save()

	print('setFilter - #### ', nome, ' ', stato, ' ', colore, ' ', filtro)
	return render(request, 'filtroButtonAgenteBack.html', {'nome' : nome, 'colore':colore, 'stato':stato, 'filtro':filtro})
#Fine codice animazioni bottoni FILTERSCREEN#######


#Funzioni di ConfigScreen
def login(request):
	#print('Questo   ', list(request.GET.lists()))
	values = list(request.GET.lists())[0][1]
	email = '' #, password = '',''
	ruolo = 0
	logged = False
	try:
		x = Utente.objects.get(email = values[0], password = values[1])
		#print(x.nome, x.email, x.password)
		if x:
			#print('esiste', x.email, x.password)
			#email = x.email
			#password= x.password
			#ruolo = x.ruolo

			request.session['email']=x.email
			#request.session['password']=x.password
			request.session['ruolo']=x.ruolo
			request.session['id']=x.id
			logged = True
			request.session.save()
			return redirect('configScreen')
		else:
			print('redirect + cambia qualcosa nella schermata')
	except ObjectDoesNotExist:
		print('Eccezione')


	return render(request, 'configScreen.html',{'email':email, 'ruolo':ruolo, 'logged':logged})

def logout(request):
	print('logout')
	lista = ['email', 'ruolo', 'listaAgenti', 'path']

	for x in lista:
		if request.session.has_key(x):
			del request.session[x]

	request.session.save()
	
	logged = False

	return render(request, 'configScreen.html',{'email': '', 'ruolo':0, 'logged':logged})

def savePath(request): #Salvataggio del path
	print('savePath')
	path = list(request.POST.lists())[0][1][0]
	print('path -- ' , path)
	#if request.session.has_key('path'):
	#	print('ho già il path')
	#else:
	request.session['path'] = path 

	lista = createListaAgenti(path)
	
	request.session['listaAgenti'] = lista

	request.session.save()

	return redirect('configScreen')

def scegliPath(request):
	print('scegli il path')
	idDirectory = request.GET['choosePath']
	dizionario = {}
	print(idDirectory) #ID Path scelto.
	try:
		xdir = Directory.objects.get(id=idDirectory)
		loc = xdir.path
	except ObjectDoesNotExist:
		print('Eccezione')
	print(loc , ' <--- PATH')

	#Quando lo scegli, ritorna l'id così da prendermi tutti gli agenti con quell'id nel DB
	try:
		lista = Agente.objects.filter(directory_id_id=idDirectory)
		for agent in lista:
			pathExist = os.path.exists(loc+agent.nome)
			#print('-----')
			#print(agent.nome)
			#print(agent.colore)
			#print(agent.stato)
			#print(agent.filtro)
			if pathExist:
				dizionario[agent.nome]=[agent.colore,agent.stato,agent.filtro]
		#print(lista)
	except ObjectDoesNotExist:
		print('Eccezione')

	request.session['listaAgenti'] = dizionario
	request.session['path'] = loc
	request.session.save()

	return redirect('configScreen')

def cancellaRunScelta(request):
	print('Cancella una run scelta tra quelle che hai fatto')
	runId = request.GET['chooseRun'] #Run scelta.
	try:
		Run.objects.get(id=runId).delete()
	except ObjectDoesNotExist:
		print('Eccezione')
	return redirect('configScreen')

def newUser(request):
	print('new User')

	return render(request, 'newUserScreen.html')

def sendNewUser(request): #Registrazione nuovo utente
	print('send New User - Registrazione nuovo utente')

	dati = list(request.POST.lists())[0][1]
	#Check delle due password: SE corrette procedi
	pswd = dati[2]
	checkPswd = dati[3]
	if pswd == checkPswd:

		try:
			print('prova')
			new = Utente(nome=dati[0], email=dati[1], password=pswd,ruolo=0)
			new.save()
			return redirect('configScreen')
		except ObjectDoesNotExist:
			print('Eccezione')

	return render(request, 'configScreen.html')