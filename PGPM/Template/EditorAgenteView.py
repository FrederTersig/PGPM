#!/usr/bin/python
# This Python file uses the following encoding: utf-8
'''
@author: Federico Tersigni
'''
import os
import sys
import justpy as jp

#Costanti delle Classi / Tailwind dei bottoni
agentiClasses = 'inline-block rounded w-32 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
agentiOnMouseOver = 'inline-block rounded w-32 h-16 bg-blue-600 m-2 text-white hover:bg-blue-400 focus:outline-white hover:text-white container'
buttonClasses = 'block rounded w-16 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
acceptClasses = 'block rounded w-16 h-16 m-2 bg-green-600 text-white hover:bg-green-300 focus:outline-white hover:text-gray-800'
rejectClasses = 'block rounded w-16 h-16 m-2 bg-red-600 text-white hover:bg-red-300 focus:outline-white hover:text-gray-800'
actionButtonClasses = 'block rounded w-32 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'


##############################


def EditorAgenteView(nomeAgente, codice, salvaCodice):
	wp = jp.WebPage()

	#print(type({request.path_params["name"]}))
	#nomeAgente = {request.path_params["name"]}.pop() <---
	#print(nomeAgente)
	#self.setNome(nomeAgente)

	wp.body_style='overflow:hidden'
	mainDiv = jp.Div(a=wp,classes='box-content bg-gray-700 h-screen border-4 w-screen flex')   
	subNavDiv = jp.Div(a=mainDiv,classes='h-64 inline-block left-0')
	####### -------> Parte Centrale: Editor
	#Frame dei bottoni
	frameDiv = jp.Div(a=mainDiv, classes='inline-block w-full h-full overflow-hidden')
	subFrameDiv = jp.Div(a=frameDiv, classes='mt-2 h-full space-y-4')
	#Parte superiore: Titolo
	titleFrameDiv = jp.Div(a=subFrameDiv, classes='block h-16 w-full pt-4')
	spanTitleFrame = jp.Span(a=titleFrameDiv, classes='align-middle')
	jp.P(a=spanTitleFrame, classes='text-center text-white font-black text-3xl subpixel-antialiased', text=nomeAgente)
	#Parte centrale: Codice                     
	#prot = jp.Div(a=wp, height='10vh')
	 
	formCode=jp.Form(a=subFrameDiv, classes='w-full h-full')            
	logFrameDiv = jp.Textarea(a=formCode,style=f'height:80%; width:100%; white-space: pre-wrap;', value=codice,classes='text-white block divide-y divide-white divide-opacity-25 w-full bg-blue-900 space-y-2 overflow-y-scroll p-2 border-2 border-white rounded-md')
	
	#editor= jp.Textarea(a=logFrameDiv, toolbar='[]', value=lunga, style=f'white-space: pre-wrap;', classes="w-full h-full") 
	#editor = jp.QEditor(a=logFrameDiv, toolbar='[]', value=lunga, style=f'white-space: pre-wrap; w-full h-full' )   # NON MOSTRA NESSUN BOTTONE SULLA TOOLBAR
		
	#Pulsantiera delle azioni del log
	#actionLogDiv = jp.Div(a=formCode, classes='block h-16 w-full')
	bottoniLogDiv = jp.Div(a=formCode, classes='flex justify-center items-center')
	saveButton = jp.Input(text='Salva', value='Salva',type='submit', a=bottoniLogDiv, classes=actionButtonClasses) #HO BISOGNO DEL CONTENT PRESENTE NELLA TEXTAREA
	backButton = jp.A(href='/start',text='Annulla', a=bottoniLogDiv, classes='text-center ' + actionButtonClasses)
	
	#Eventuale altra fila di bottoni
	####### -------> Fine Parte Centrale: Log
	####### -------> Parte Destra: Tasto Filtro
	formCode.on('submit',salvaCodice)
		
		
	return wp