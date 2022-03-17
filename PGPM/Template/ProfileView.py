#!/usr/bin/python
# This Python file uses the following encoding: utf-8
'''
@author: Federico Tersigni
'''
import os
import sys
import justpy as jp

from Template.icons.iconList import logIcon
from Template.icons.iconList import configIcon
from Template.icons.iconList import backendIcon
from Template.icons.iconList import startRunIcon
from Template.icons.iconList import editorAgenteIcon
from Template.icons.iconList import disattivaStatoIcon
from Template.icons.iconList import attivaStatoIcon
from Template.icons.iconList import cancellaAgenteIcon
from Template.icons.iconList import filtroIcon

coloreAgente = 'background-color:'
agentiClasses = 'inline-block truncate text-center dis rounded w-48 h-20 m-2 bg-[#333333] border-white border text-white'
agentiOnMouseOver = 'inline-block truncate text-center rounded w-48 h-20 m-2 bg-[#FFFFFF] text-black border-black border container'
buttonClasses = 'block rounded w-16 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
acceptClasses = 'block rounded w-16 h-16 m-2 bg-green-600 text-white hover:bg-green-300 focus:outline-white hover:text-gray-800'
rejectClasses = 'block rounded w-16 h-16 m-2 bg-red-600 text-white hover:bg-red-300 focus:outline-white hover:text-gray-800'
actionButtonClasses = 'block rounded w-32 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'

def ProfileView(emailUpdateEvent, pswdUpdateEvent, accountDeleteEvent, sessione):
	wp = jp.WebPage()
	wp.body_style='overflow:hidden'
	mainDiv = jp.Div(a=wp,classes='box-content bg-gray-700 h-screen border-4 w-screen flex')
	####### -------> Pulsantiera Sinistra
	subNavDiv = jp.Div(a=mainDiv,classes='h-64 inline-block left-0')
	#- icona per il tasto del menu start -# IN QUESTO CASO, QUESTO BOTTONE E' DISABLED
	#initButtonNav = jp.Button(a=subNavDiv, classes=buttonClasses)
	#- icona per il tasto del menu log -#
	#logButtonNav = jp.A(href='/log/', a=subNavDiv, classes=buttonClasses, inner_html=logIcon())
	filterButton = jp.A(href='/filter/', a=subNavDiv, classes=buttonClasses, inner_html=filtroIcon())
	#logButtonNav = jp.Button(a=subNavDiv, classes=buttonClasses)
	#- icona per il tasto di configurazione -#
	configButtonNav = jp.A(href='/config/', a=subNavDiv, classes=buttonClasses, inner_html=configIcon())
	if 'logged_in' in sessione and sessione['logged_in']:
		#if sessione['utente'][4] == 1:
		if 'utente' in sessione and sessione['utente'][4] ==1:
			#- icona per il tasto di Backend -# VISTO SOLO DA ADMIN
			backendButtonNav = jp.A(href='/backend/', a=subNavDiv, classes=buttonClasses, inner_html=backendIcon())
			####### -------> Fine Pulsantiera Sinistra


	####### -------> Parte Centrale: Log
	#Frame dei bottoni
	frameDiv = jp.Div(a=mainDiv, classes='inline-block w-full h-full overflow-hidden')
	subFrameDiv = jp.Div(a=frameDiv, classes='mt-2 h-full space-y-4')
	#Parte superiore: Titolo
	titleFrameDiv = jp.Div(a=subFrameDiv, classes='block h-16 w-full pt-3')
	spanTitleFrame = jp.Span(a=titleFrameDiv, classes='align-middle')
	jp.P(a=spanTitleFrame, classes='text-center font-black text-3xl subpixel-antialiased text-white', text='Profilo Utente')
	#Div - Div if
	divShowUt = jp.Div(a=titleFrameDiv, classes='w-full flex justify-between')
	divLeftUt = jp.Div(a=divShowUt, classes='text-left inline-block')
	#if con p
	if 'utente' in sessione:
		ut_email = sessione['utente'][2]
		jp.P(a=divLeftUt, classes='m-1 text-white font-black text-left',text='Connesso come: '+ut_email)
	else:
		jp.P(a=divLeftUt, classes='m-1 text-white font-black text-left', text='Visitatore, registrati o fai il login!')
	
	divRightUt = jp.Div(a=divShowUt, classes='text-right inline-block')
	#if con p
	if 'path' in sessione and 'nome_path' in sessione:
		pathString = 'Nome del Path:'+sessione['nome_path']+' - Path Inserito: '+sessione['path']
		jp.P(a=divRightUt, classes='m-1 text-white font-black text-left',text=pathString)
	else:
		jp.P(a=divRightUt, classes='m-1 text-white font-black text-left', text='Nessun Path Inserito')

	### -- > < -- ###
	logFrameDiv = jp.Div(a=subFrameDiv,style=f'height:80%; width:100%;', classes='w-full bg-blue-900 p-2 border-2 border-white rounded-mdr')

	#Prima Riga
	divShowUt = jp.Div(a=logFrameDiv, classes='w-full flex justify-around border-white border  my-4 bg-gray-600 bg-opacity-25 rounded')
	divLeft = jp.Div(a=divShowUt, classes='w-50 h-50 block')
	divBlockName = jp.Div(a=divLeft,classes='block')
	visualNick = 'Nickname: '+ sessione['utente'][1]
	jp.P(a=divBlockName, classes='inline-block text-center font-black text-2xl subpixel-antialiased text-white py-2', text=visualNick)
	#jp.P(a=divBlockName, classes='inline-block text-center font-black text-2xl subpixel-antialiased text-white', text=f'Federico')
	#divBlockSurname = jp.Div(a=divLeft,classes='block')

	#jp.P(a=divBlockSurname, classes='inline-block text-center font-black text-2xl subpixel-antialiased text-white py-2', text=f'Cognome: Tersigni')
	#jp.P(a=divBlockSurname, classes='inline-block text-center font-black text-2xl subpixel-antialiased text-white', text=f'Federico')

	divRight = jp.Div(a=divShowUt, classes='w-50 h-50 block')
	divBlockEmail = jp.Div(a=divRight,classes='block')
	visualEmail = 'Email: '+ sessione['utente'][2]
	jp.P(a=divBlockEmail, classes='inline-block text-center font-black text-2xl subpixel-antialiased text-white py-2', text=visualEmail)
	#jp.P(a=divBlockEmail, classes='inline-block text-center font-black text-2xl subpixel-antialiased text-white', text=f'Federico')
	divBlockRuolo = jp.Div(a=divRight,classes='block')
	if sessione['utente'][4]==1:
		visualRuolo = 'Ruolo: Amministratore'
	else:
		visualRuolo = 'Ruolo: Utente'
	jp.P(a=divBlockRuolo, classes='inline-block text-center font-black text-2xl subpixel-antialiased text-white py-2', text=visualRuolo)
	#jp.P(a=divBlockRuolo, classes='inline-block text-center font-black text-2xl subpixel-antialiased text-white', text=f'Federico')

	#Seconda Riga

	formEditEmail = jp.Form(a=logFrameDiv, classes='block w-full  border-white border my-4 bg-gray-600 bg-opacity-25 rounded')
	jp.P(a=formEditEmail, classes='block w-full text-center font-black text-2xl subpixel-antialiased text-white',text='Modifica Email')
	mainDivFormEmail = jp.Div(a=formEditEmail, classes='w-full flex justify-around')
	
	editDivLeft = jp.Div(a=mainDivFormEmail, classes='block w-50 h-50')
	emailPswdLabel = jp.Label(a=editDivLeft,classes='block text-white font-black py-2',text='Password')
	emailPswdInput = jp.Input(a=editDivLeft, id='pswdEditEmail', name='pswdEditEMail', type='text', placeholder='Inserisci Password', classes='block form-input my-1 w-full')
	emailPswdLabel.for_component = emailPswdInput

	editDivRight = jp.Div(a=mainDivFormEmail, classes='block w-50 h-50')
	emailEditLabel = jp.Label(a=editDivRight,classes='block text-white font-black py-2',text='Email')
	emailEditInput = jp.Input(a=editDivRight, id='emailEditEmail', name='emailEditEMail', type='text', placeholder='Inserisci Email', classes='block form-input my-1 w-full')
	emailEditLabel.for_component = emailEditInput

	divButtonEmail = jp.Div(a=formEditEmail,classes='w-full h-50 flex justify-center')
	submitEmail = jp.Input(a=divButtonEmail, type='submit', value='Modifica', classes='block rounded w-1/3 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800')
	formEditEmail.on('submit',emailUpdateEvent)

	#Terza Riga

	formEditPswd = jp.Form(a=logFrameDiv, classes='block w-full border-white border my-4 bg-gray-600 bg-opacity-25 rounded')
	jp.P(a=formEditPswd , classes='block w-full text-center font-black text-2xl subpixel-antialiased text-white',text='Modifica Password')
	mainDivForPswd = jp.Div(a=formEditPswd, classes='w-full flex justify-around')

	editPswdLeft = jp.Div(a=mainDivForPswd, classes='block w-50 h-50')
	oldPswdLabel = jp.Label(a=editPswdLeft,classes='block text-white font-black py-2',text='Vecchia Password')
	oldPswdInput = jp.Input(a=editPswdLeft, id='oldPswd', name='oldPswd', type='text', placeholder='Inserisci Vecchia Password', classes='block form-input my-1 w-full')
	oldPswdLabel.for_component = oldPswdInput

	editPswdRight = jp.Div(a=mainDivForPswd, classes='block w-50 h-50')
	pswdEditLabel = jp.Label(a=editPswdRight,classes='block text-white font-black py-2',text='Nuova Password')
	pswdEditInput = jp.Input(a=editPswdRight, id='newPswd', name='newPswd', type='text', placeholder='Inserisci Nuova Password', classes='block form-input my-1 w-full')
	pswdEditLabel.for_component = pswdEditInput

	divButtonPswd = jp.Div(a=formEditPswd,classes='w-full h-50 flex justify-center')
	submitPswd = jp.Input(a=divButtonPswd, type='submit', value='Modifica', classes='block rounded w-1/3 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800')
	formEditPswd.on('submit',pswdUpdateEvent)
	

	#Quarta Riga
	x_idUtente = sessione['utente'][0]
	divMainCancella = jp.Div(a=logFrameDiv, classes='w-full block border-white border  bg-gray-600 bg-opacity-25 rounded')
	jp.P(a=divMainCancella, classes='block w-full text-center font-black text-2xl subpixel-antialiased text-white',text='Cancellazione Account Dal Sistema')
	divCancella = jp.Div(a=divMainCancella, classes='w-full h-1/2 flex justify-center my-4')
	buttonCancellaUt = jp.Button(a=divCancella, click=accountDeleteEvent,idUtente=x_idUtente, text='Cancella Account', classes='block rounded w-1/3 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800  content-end')
	#Cancella attuale utente

	return wp