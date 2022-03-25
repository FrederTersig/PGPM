#!/usr/bin/python
# This Python file uses the following encoding: utf-8
'''
@author: Federico Tersigni
'''

import justpy as jp
import sys
from Model.Run import Run
from Model.Directory import Directory

from Template.icons.iconList import startIcon
from Template.icons.iconList import filtroIcon
from Template.icons.iconList import backendIcon
from Template.icons.iconList import newUserIcon
from Template.icons.iconList import profileIcon


infoRegTesto='Se si vuole creare un nuovo account nel sistema, si può cliccare questo pulsante per raggiungere la pagina di registrazione.'
#Costanti delle Classi / Tailwind dei bottoni
agentiClasses = 'inline-block rounded w-32 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
agentiOnMouseOver = 'inline-block rounded w-32 h-16 bg-blue-600 m-2 text-white hover:bg-blue-400 focus:outline-white hover:text-white container'
buttonClasses = 'block rounded w-16 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
acceptClasses = 'block rounded w-16 h-16 m-2 bg-green-600 text-white hover:bg-green-300 focus:outline-white hover:text-gray-800'
rejectClasses = 'block rounded w-16 h-16 m-2 bg-red-600 text-white hover:bg-red-300 focus:outline-white hover:text-gray-800'
actionButtonClasses = 'block rounded w-32 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'

passwordClasses= ''
#Codice della grafica della schermata di Configurazione


############################################
def ConfigView(dirs,runs,loginEvent,savePathEvent,logoutEvent,sceltaRunCanc,sceltaPath,s):
	wp = jp.WebPage()
	wp.body_style='overflow:hidden'
	mainDiv = jp.Div(a=wp,classes='box-content bg-gray-700 h-screen border-4 w-screen flex')   
	####### -------> Pulsantiera Sinistra
	subNavDiv = jp.Div(a=mainDiv,classes='h-64 inline-block left-0')
	#- icona per il tasto del menu start -#
	#initButtonNav = jp.Div(a=subNavDiv, classes=buttonClasses)
	initButtonNav = jp.A(href='/start', a=subNavDiv, classes=buttonClasses, inner_html=startIcon())
	#- icona per il tasto del menu log -#
	filterButton = jp.A(href='/filter/', a=subNavDiv, classes=buttonClasses, inner_html=filtroIcon())
	#- icona per il tasto di configurazione -# DISABILITATO
	#- icona per il tasto di Backend -# VISTO SOLO DA ADMIN
	if s['logged_in']:
		profileButtonNav = jp.A(href='/profile/',a=subNavDiv, classes=buttonClasses, inner_html=profileIcon())
		if s['utente'][4] == 1:
			backendButtonNav = jp.A(href='/backend/', a=subNavDiv, classes=buttonClasses, inner_html=backendIcon())
	####### -------> Fine Pulsantiera Sinistra

	####### -------> Parte Centrale: CONFIGURAZIONE
	#Frame dei bottoni
	frameDiv = jp.Div(a=mainDiv, classes='inline-block w-full h-full overflow-hidden')
	subFrameDiv = jp.Div(a=frameDiv, classes='mt-2 h-full space-y-4')
	#Parte superiore: Titolo
	titleFrameDiv = jp.Div(a=subFrameDiv, classes='block h-16 w-full pt-3')
	spanTitleFrame = jp.Span(a=titleFrameDiv, classes='align-middle')
	jp.P(a=spanTitleFrame, classes='text-center font-black text-3xl subpixel-antialiased text-white', text='Schermata di configurazione')
	### -- > < -- ###
	#Div - Div if
	divShowUt = jp.Div(a=titleFrameDiv, classes='w-full flex justify-between')
	divLeftUt = jp.Div(a=divShowUt, classes='text-left inline-block')
	#if con p
	if 'utente' in s:
		#print(s['utente'],'  ',type(s['utente']))
		ut_email = s['utente'][2]
		jp.P(a=divLeftUt, classes='m-1 text-white font-black text-left',text='Connesso come: '+ut_email)
	else:
		jp.P(a=divLeftUt, classes='m-1 text-white font-black text-left', text='Visitatore, registrati o fai il login!')
	
	divRightUt = jp.Div(a=divShowUt, classes='text-right inline-block')
	#if con p
	if 'path' in s and 'nome_path' in s:
		pathString = 'Nome del Path:'+s['nome_path']+' - Path Inserito: '+s['path']
		jp.P(a=divRightUt, classes='m-1 text-white font-black text-left',text=pathString)
	else:
		jp.P(a=divRightUt, classes='m-1 text-white font-black text-left', text='Nessun Path Inserito')

	### -- > < -- ###
	#Parte centrale: Lista delle form #################################################                         
	formFrameDiv = jp.Div(a=subFrameDiv,style=f'height:80%; width:100%;', classes='block bg-blue-900 p-2 border-2 border-white rounded-md')
	############################################################
	#Sezione di autenticazione / Registrazione nuovo utente -->
	sezAutRegDiv = jp.Div(a=formFrameDiv, classes='block border m-10 p-2 flex flex-row')
	sezAutDiv = jp.Div(a=sezAutRegDiv, classes='inline-block border basis-1/2 w-full')
	jp.P(a=sezAutDiv, classes='text-white font-black text-left px-6 py-2 text-2xl subpixel-antialiased', text='Autenticazione')

	if s['logged_in'] is True:
		sezAutRow = jp.Div(classes='flex flex-row items-center p-4', a=sezAutDiv)
		sezAutLogInfo = jp.Div(a=sezAutRow, classes='basis-5/6 w-full p-2')
		jp.P(a=sezAutLogInfo, classes='text-white font-black inline-block', text=f"Connesso con l'account: "+s['utente'][2])

		sezAutLogInfo_B = jp.Div(a=sezAutRow, classes='basis-1/6 w-3/6 mr-4')
		sezAutLogoutButton = jp.Button(a=sezAutLogInfo_B, classes='block rounded w-full h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800', text='Logout', click=logoutEvent)

	else:
		sezLoginForm = jp.Form(a=sezAutDiv, classes='block h-full w-full')
		sezLoginFormDiv = jp.Div(a=sezLoginForm, classes='flex flex-row items-center p-4')
		sezLoginFormDivLeftLabel = jp.Div(a=sezLoginFormDiv, classes='basis-2/6 left-0 p-2')
		
		labelEmailInput = jp.Label(a=sezLoginFormDivLeftLabel, classes='text-white font-black py-2', text='Email')
		labelPasswordInput = jp.Label(a=sezLoginFormDivLeftLabel, classes='text-white font-black py-2', text='Password')

		sezLoginFormDivLeftInput = jp.Div(a=sezLoginFormDiv, classes='basis-3/6')

		loginEmailInput = jp.Input(a=sezLoginFormDivLeftInput,id='email', type='text', placeholder='Inserisci un email', classes='form-input my-1 w-full', name='login')
		loginPasswordInput = jp.Input(a=sezLoginFormDivLeftInput,id='password', type='password', placeholder='Password', classes='form-input my-1 w-full font-black', name='login')

		labelEmailInput.for_component = loginEmailInput
		labelPasswordInput.for_component = loginPasswordInput

		sezLoginFormDivLeftSubmit = jp.Div(a=sezLoginFormDiv, classes='basis-1/6 w-1/3 mr-4')
		loginSubmitInput = jp.Input(a=sezLoginFormDivLeftSubmit, type='submit', value='Login', classes='block rounded w-full h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800')
		sezLoginForm.on('submit',loginEvent)

	#Parte Registrazione
	sezRegDiv = jp.Div(a=sezAutRegDiv, classes='inline-block border basis-1/2 w-full')
	jp.P(text='Registrazione', a=sezRegDiv, classes='text-white font-black text-left px-6 py-2 text-2xl subpixel-antialiased')
	sezRegDivSub = jp.Div(a=sezRegDiv,classes='flex flex-row items-center p-4')
	sezRegDivSubPDiv = jp.Div(a=sezRegDivSub, classes='basis-5/6 w-full p-2')
	jp.P(a=sezRegDivSubPDiv, classes='text-white font-black inline-block text-left',text=infoRegTesto)

	sezRegDivSubButtonDiv = jp.Div(a=sezRegDivSub, classes='basis-1/6 w-3/6 mr-4')
	creaUtenteButton = jp.A(href='/config/newUser/',a=sezRegDivSubButtonDiv, classes='block rounded w-full h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800 flex flex-row items-center')
	creaUtenteButtonIconDiv = jp.Div(a=creaUtenteButton,classes='basis-1/5 inline-block',inner_html=newUserIcon())
	creaUtenteButtonTesto = jp.Div(a=creaUtenteButton, classes='basis-4/5 inline-block', text='Crea Nuovo Utente')


	#############################
	#Sezione di salvataggio Path/
	if s['logged_in'] is True:
		partDir = jp.Div(a=formFrameDiv, classes='block border m-10 p-2 flex flex-row')
		partDirSave = jp.Div(a=partDir, classes='inline-block border basis-1/2 w-full')
		jp.P(a=partDirSave,classes='text-white font-black text-left px-6 py-2 text-2xl subpixel-antialiased',text='Salva Nuova Directory')
		saveForm = jp.Form(a=partDirSave,method='post', classes='block h-full w-full', id='directoryForm')
		saveFormMainDiv = jp.Div(a=saveForm,classes='flex flex-row items-center p-4')
		saveFormFirstSect = jp.Div(a=saveFormMainDiv, classes='basis-2/6 left-0 p-2')
		##
		saveDirPathLabel = jp.Label(a=saveFormFirstSect,classes='text-white font-black py-2',text='Directory Path')
		saveDirNomeLabel = jp.Label(a=saveFormFirstSect,classes='text-white font-black py-2',text='Nome')
		##
		saveFormSecondSect = jp.Div(a=saveFormMainDiv, classes='basis-3/6')
		saveInputPath = jp.Input(a=saveFormSecondSect, id='path', name='_path', type='text', placeholder='Path', classes='form-input my-1 w-full')
		saveNomePath = jp.Input(a=saveFormSecondSect,id='nome', type='text', placeholder='Nome', classes='form-input my-1 w-full', name='_path')
		
		saveDirPathLabel.for_component=saveInputPath
		saveDirNomeLabel.for_component=saveNomePath

		saveFormThirdSect = jp.Div(a=saveFormMainDiv, classes='basis-1/6 w-1/3 mr-4')
		saveFormSubmit = jp.Input(a=saveFormThirdSect, type='submit', value='Salva', classes='block rounded w-full h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800')

		saveForm.on('submit',savePathEvent)
		##############

		partLoadDir = jp.Div(a=partDir,classes='inline-block border basis-1/2 w-full')
		jp.P(a=partLoadDir,text='Carica Vecchia Directory',classes='text-white font-black text-left px-6 py-2 text-2xl subpixel-antialiased')
		loadMainDiv = jp.Div(a=partLoadDir, classes='flex flex-row items-center p-4 w-full')
		loadFirstSec = jp.Div(a=loadMainDiv,classes='basis-5/6 w-full p-2')
		
		loadSecondSec = jp.Div(a=loadMainDiv,classes='basis-1/6 w-3/6 mr-4')
		if dirs:
			loadForm = jp.Form(a=loadSecondSec,method='get', id='formChoosePath', classes='inline-block w-full')

			loadSelect = jp.Select(a=loadFirstSec, form=loadForm,classes='inline-block font-black text-black px-4 form-input')
			for y in dirs:
				stringa = 'ID: '+str(y.getId())+' '+y.getNome()+' : '+y.getPath()+'UTENTE_ID: '+str(y.getUtente_id())
				loadSelect.add(jp.Option(value=[y.getId(),y.getPath(),y.getNome()], text=stringa, classes='font-black'))
				jp.Input(a=loadForm,type='hidden', value=y.getId(), id=y.getId(), name='ID')
				jp.Input(a=loadForm,type='hidden', value=y.getPath(), name='PATH')
				jp.Input(a=loadForm,type='hidden', value=y.getNome(), name='NOME')
				jp.Input(a=loadForm,type='hidden', value=y.getUtente_id(), name='UTENTEID')
			###
			loadSubmitInput = jp.Input(a=loadForm, type='submit', value='scegli', classes='block rounded w-full h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800 flex flex-row items-center', style='width:70px;')#formChoosePath
			loadForm.on('submit',sceltaPath)
		else:
			jp.P(a=loadFirstSec, text='Nessuna Directory usata.', classes='text-white font-black text-left')
		#Ultima sezione di gestione Run
		flexRun = jp.Div(a=formFrameDiv, classes='flex justify-around')
		partRun = jp.Div(a=flexRun,classes='block border m-10 p-2 flex flex-row') #part run
		partDeleteRun = jp.Div(a=partRun, classes='inline-block border basis-1/2 w-full')
		jp.P(a=partDeleteRun, text='Cancella Specifica Run',classes='text-white font-black text-left px-6 py-2 text-2xl subpixel-antialiased')
		pDR_Div = jp.Div(a=partDeleteRun, classes='flex flex-row items-center p-4')
		pDR_first = jp.Div(a=pDR_Div, classes='basis-5/6 w-full p-2')
		if runs:
			
			# Qui select
			runSelect = jp.Select(a=pDR_first, classes='inline-block', form='cancellaRunForm')
			####
			for run in runs:
				stringa = 'ID: '+str(run.getId())+' TIMESTAMP: '+run.getTimestamp()+'UTENTE_ID: '+str(run.getUtente_id())+' DIRECTORY_ID: '+str(run.getDirectory_id())
				runSelect.add(jp.Option(value=run.getId(), text=stringa, classes='font-black'))
			###
			pDR_Second = jp.Div(a=pDR_Div,classes='basis-1/6 w-3/6 mr-4')
			#if runs:
			cancellaRunForm = jp.Form(a=pDR_Second,method='get', id='cancellaRunForm', classes='inline-block w-full')
				
			inputDelRunForm = jp.Input(a=cancellaRunForm,type='submit', value='cancella', classes='block rounded w-full h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800 flex flex-row items-center', style='width:70px;')
		else:
			jp.P(a=pDR_first, text='Nessuna Run eseguita.',classes='text-white font-black text-left')

	#Fine sezioni complesse
	########################
	########################

		
	return wp