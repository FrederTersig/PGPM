#!/usr/bin/python
# This Python file uses the following encoding: utf-8
'''
@author: Federico Tersigni
'''

import justpy as jp
from Engine.Agente import Agente

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
timestamp = 'TimeStamp'
message = 'Message'
nomeAgente = 'Nome Agente'
############################################

class LogScreen:
    def logScreen(self):
        wp = jp.WebPage()
        wp.body_style='overflow:hidden'
        mainDiv = jp.Div(a=wp,classes='box-content bg-gray-700 h-screen border-4 w-screen flex')   
        ####### -------> Pulsantiera Sinistra
        subNavDiv = jp.Div(a=mainDiv,classes='h-64 inline-block left-0')
        #- icona per il tasto del menu start -#
        #initButtonNav = jp.Div(a=subNavDiv, classes=buttonClasses)
        initButtonNav = jp.A(href='/start', a=subNavDiv, classes=buttonClasses)
        menuStartIcon = jp.Svg(a=initButtonNav,viewBox='0 -2 16 20', xmlns='http://www.w3.org/2000/svg', classes='bi bi-play-circle', fill='currentColor',width='64',height='64')
        pathStartIconA = jp.Path(d='M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z', a=menuStartIcon)
        pathStartIconB = jp.Path(d='M6.271 5.055a.5.5 0 0 1 .52.038l3.5 2.5a.5.5 0 0 1 0 .814l-3.5 2.5A.5.5 0 0 1 6 10.5v-5a.5.5 0 0 1 .271-.445z', a=menuStartIcon)
        #- icona per il tasto del menu log -# -- DISABILITATO
        logButtonNav = jp.Div(a=subNavDiv, classes=buttonClasses)
        logIcon = jp.Svg(a=logButtonNav, viewBox='0 -2 16 20', xmlns='http://www.w3.org/2000/svg', classes='bi bi-chat-right-text', fill='currentColor',width='64',height='64')
        logIconPathA = jp.Path(d='M2 1a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h9.586a2 2 0 0 1 1.414.586l2 2V2a1 1 0 0 0-1-1H2zm12-1a2 2 0 0 1 2 2v12.793a.5.5 0 0 1-.854.353l-2.853-2.853a1 1 0 0 0-.707-.293H2a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h12z',a=logIcon)
        logIconPathB = jp.Path(d='M3 3.5a.5.5 0 0 1 .5-.5h9a.5.5 0 0 1 0 1h-9a.5.5 0 0 1-.5-.5zM3 6a.5.5 0 0 1 .5-.5h9a.5.5 0 0 1 0 1h-9A.5.5 0 0 1 3 6zm0 2.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1-.5-.5z',a=logIcon)
        #- icona per il tasto di configurazione -#
        configButtonNav = jp.Div(a=subNavDiv, classes=buttonClasses)
        configIcon = jp.Svg(a=configButtonNav, viewBox='0 -2 16 20', xmlns='http://www.w3.org/2000/svg', classes='bi bi-gear-fill', fill='currentColor',width='64',height='64')
        configIconPathA = jp.Path(d='M9.405 1.05c-.413-1.4-2.397-1.4-2.81 0l-.1.34a1.464 1.464 0 0 1-2.105.872l-.31-.17c-1.283-.698-2.686.705-1.987 1.987l.169.311c.446.82.023 1.841-.872 2.105l-.34.1c-1.4.413-1.4 2.397 0 2.81l.34.1a1.464 1.464 0 0 1 .872 2.105l-.17.31c-.698 1.283.705 2.686 1.987 1.987l.311-.169a1.464 1.464 0 0 1 2.105.872l.1.34c.413 1.4 2.397 1.4 2.81 0l.1-.34a1.464 1.464 0 0 1 2.105-.872l.31.17c1.283.698 2.686-.705 1.987-1.987l-.169-.311a1.464 1.464 0 0 1 .872-2.105l.34-.1c1.4-.413 1.4-2.397 0-2.81l-.34-.1a1.464 1.464 0 0 1-.872-2.105l.17-.31c.698-1.283-.705-2.686-1.987-1.987l-.311.169a1.464 1.464 0 0 1-2.105-.872l-.1-.34zM8 10.93a2.929 2.929 0 1 1 0-5.86 2.929 2.929 0 0 1 0 5.858z',a=configIcon)
        ####### -------> Fine Pulsantiera Sinistra
        ####### -------> Parte Centrale: Log
        #Frame dei bottoni
        frameDiv = jp.Div(a=mainDiv, classes='inline-block w-full h-full overflow-hidden')
        subFrameDiv = jp.Div(a=frameDiv, classes='mt-2 h-full space-y-4')
        #Parte superiore: Titolo
        titleFrameDiv = jp.Div(a=subFrameDiv, classes='block h-16 w-full pt-4')
        spanTitleFrame = jp.Span(a=titleFrameDiv, classes='align-middle')
        jp.P(a=spanTitleFrame, classes='text-center font-black text-3xl subpixel-antialiased text-white', text='Schermata dei Log')
        #Parte centrale: Lista degli output                                             
        logFrameDiv = jp.Div(a=subFrameDiv,style=f'height:80%; width:100%;', classes='block divide-y divide-white divide-opacity-25 w-full bg-blue-900 space-y-2 overflow-y-scroll p-2 border-2 border-white rounded-md')
        jp.P(a=logFrameDiv, classes='subpixel-antialiased text-white break-words', text='> '+timestamp+' | '+message+' | '+nomeAgente)
        #Pulsantiera delle azioni del log
        actionLogDiv = jp.Div(a=subFrameDiv, classes='block h-16 w-full')
        bottoniLogDiv = jp.Div(a=actionLogDiv, classes='block flex justify-around')
        exportLogButton = jp.Button(text='Esporta Log', a=bottoniLogDiv, classes=actionButtonClasses)
        cleanLogButton = jp.Button(text='Pulisci Tutto', a=bottoniLogDiv, classes=actionButtonClasses)
        #Eventuale altra fila di bottoni
        ####### -------> Fine Parte Centrale: Log
        ####### -------> Parte Destra: Tasto Filtro
        #Menu Destro (Tasto del filtro)
        filterNavDiv = jp.Div(a=mainDiv,classes='h-64 inline-block w-22') #Aumento la width così da sistemare al meglio la posizione dei bottoni
        filterButton = jp.A(href='/filter', a=filterNavDiv, classes=buttonClasses)
        # filterButton = jp.Div(a=filterNavDiv, classes=buttonClasses)
        filterIcon = jp.Svg(a=filterButton, viewBox='0 -2 16 20', xmlns='http://www.w3.org/2000/svg', classes='bi bi-chat-funnel-fill', fill='currentColor',width='64',height='64')
        filterPathIconA = jp.Path(d='M1.5 1.5A.5.5 0 0 1 2 1h12a.5.5 0 0 1 .5.5v2a.5.5 0 0 1-.128.334L10 8.692V13.5a.5.5 0 0 1-.342.474l-3 1A.5.5 0 0 1 6 14.5V8.692L1.628 3.834A.5.5 0 0 1 1.5 3.5v-2z',a=filterIcon)
        ####### -------> Fine Parte Destra: Tasto Filtro
        
        return wp