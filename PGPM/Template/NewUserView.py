#!/usr/bin/python
# This Python file uses the following encoding: utf-8
'''
@author: Federico Tersigni
'''
import justpy as jp
import sys


from Template.icons.iconList import startIcon
from Template.icons.iconList import filtroIcon
#from Template.icons.iconList import logIcon
from Template.icons.iconList import configIcon
from Template.icons.iconList import backendIcon
from Template.icons.iconList import annullaIcon
from Template.icons.iconList import profileIcon

#Costanti delle Classi / Tailwind dei bottoni
agentiClasses = 'inline-block rounded w-32 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
agentiOnMouseOver = 'inline-block rounded w-32 h-16 bg-blue-600 m-2 text-white hover:bg-blue-400 focus:outline-white hover:text-white container'
buttonClasses = 'block rounded w-16 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
acceptClasses = 'block rounded w-16 h-16 m-2 bg-green-600 text-white hover:bg-green-300 focus:outline-white hover:text-gray-800'
rejectClasses = 'block rounded w-16 h-16 m-2 bg-red-600 text-white hover:bg-red-300 focus:outline-white hover:text-gray-800'
actionButtonClasses = 'block rounded w-32 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
#Codice della grafica della schermata di NewUser

############################################

def NewUserView(creaUtente,s):
	print('NEWUSERSCREEN')
	wp = jp.WebPage()
	wp.body_style='overflow:hidden'
	mainDiv = jp.Div(a=wp,classes='box-content bg-gray-700 h-screen border-4 w-screen flex')   
	####### -------> Pulsantiera Sinistra
	#subNavDiv = jp.Div(a=mainDiv,classes='h-64 inline-block left-0')
	#- icona per il tasto del menu start -#
	#initButtonNav = jp.Div(a=subNavDiv, classes=buttonClasses)
	#initButtonNav = jp.A(href='/start/', a=subNavDiv, classes=buttonClasses, inner_html=startIcon())
	#- icona per il tasto del menu log -# -- DISABILITATO
	#filterButton = jp.A(href='/filter/', a=subNavDiv, classes=buttonClasses, inner_html=filtroIcon())
	#- icona per il tasto di configurazione -#
	#configButtonNav = jp.A(href='/config/', a=subNavDiv, classes=buttonClasses, inner_html=configIcon())
	#- icona per il tasto di Backend -# VISTO SOLO DA ADMIN
	#if s['logged_in']:
	#	profileButtonNav = jp.A(href='/profile/',a=subNavDiv, classes=buttonClasses, inner_html=profileIcon())
	#	if s['utente'][4] == 1:
	#		backendButtonNav = jp.A(href='/backend/', a=subNavDiv, classes=buttonClasses, inner_html=backendIcon())
	####### -------> Fine Pulsantiera Sinistra

	####### -------> Parte Centrale: Creazione Nuovo Utente

	frameDiv = jp.Div(a=mainDiv, classes='inline-block w-full h-full overflow-hidden')
	subFrameDiv = jp.Div(a=frameDiv, classes='mt-2 h-full space-y-4')
	#Parte superiore: Titolo
	titleFrameDiv = jp.Div(a=subFrameDiv, classes='block h-16 w-full pt-4')
	spanTitleFrame = jp.Span(a=titleFrameDiv, classes='align-middle')
	jp.P(a=spanTitleFrame, classes='text-center font-black text-3xl subpixel-antialiased text-white', text='Registra Nuovo Utente')
	#Parte centrale della creazione nuovo utente  
	


	## CREAZIONE NUOVO UTENTE ##
	newUserDiv = jp.Div(a=subFrameDiv, style=f'height:80%; width:100%', classes='block w-full bg-blue-900 space-y-2 overflow-y-scroll p-2 border-2 border-white rounded-md')

	divFirst = jp.Div(a=newUserDiv, classes='pt-36 flex justify-around')
	divSecond = jp.Div(a=divFirst, classes='block border m-2 p-2 flex')
	divThird = jp.Div(a=divSecond, classes='block border w-full')
	jp.P(a=divThird, classes='text-white font-black text-center px-6 py-2 text-2xl subpixel-antialiased', text='Compila i campi')
	newUserForm = jp.Form(a=divThird, classes='block p-2 flex  items-center', style='height:80%; width:80%;')
	groupADiv =jp.Div(a=newUserForm, classes='p-4')

	nomeLabel = jp.Label(text='Nickname: ', a=groupADiv, classes='text-white font-black px-4')
	nomeInput = jp.Input(placeholder='Nickname', a=groupADiv, classes='block form-input px-4')
	nomeLabel.for_component = nomeInput

	emailLabel = jp.Label(text='Email: ', a=groupADiv, classes='text-white font-black px-4')
	emailInput = jp.Input(placeholder='Email', a=groupADiv, classes='fblock form-input px-4')
	emailLabel.for_component = emailInput
	
	passwordLabel = jp.Label(text='Password: ', a=groupADiv, classes='text-white font-black px-4')
	passwordInput = jp.Input(placeholder='Password', a=groupADiv, classes='block form-input px-4',type='password')
	passwordLabel.for_component = passwordInput

	confPasswordLabel = jp.Label(text='Conferma Password: ', a=groupADiv, classes='text-white font-black px-4')
	confPasswordInput = jp.Input(placeholder='Conferma Password', a=groupADiv, classes='block form-input px-4',type='password')
	confPasswordLabel.for_component = confPasswordInput                                      

	divFourth = jp.Div(a=newUserForm, classes='w-full')
	newUserButton = jp.Input(value='Crea Nuovo Utente', type='submit', a=newUserForm, classes='rounded w-48 h-32 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800')

	newUserForm.on('submit', creaUtente)
	####### -------> Fine Parte Centrale

	divUltButton = jp.Div(a=subFrameDiv, classes='block flex justify-around h-24 w-full')
	ultButton = jp.A(a=divUltButton,href='/config/', classes='block rounded w-32 h-16 m-2 bg-blue-600 text-white text-center hover:bg-white focus:outline-white hover:text-gray-800', text='Torna Indietro')

	####### -------> Parte Destra: Tasti di gestione del db
	#Menu Destro (Tasto del filtro)
	#newUserNavDiv = jp.Div(a=mainDiv,classes='h-64 inline-block w-22') #Aumento la width così da sistemare al meglio la posizione dei bottoni
	#rejectButton = jp.A(href='/config/', a=newUserNavDiv, classes=rejectClasses, inner_html=annullaIcon())


	####### -------> Fine Parte Destra
		
	return wp