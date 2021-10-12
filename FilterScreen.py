#!/usr/bin/python
# This Python file uses the following encoding: utf-8
'''
@author: Federico Tersigni
'''

import justpy as jp
from Engine import Agente as agent
#from Engine.Agente import Agente

#Costanti delle Classi / Tailwind dei bottoni
agentiClasses = 'inline-block rounded w-32 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
agentiOnMouseOver = 'inline-block rounded w-32 h-16 bg-blue-600 m-2 text-white hover:bg-blue-400 focus:outline-white hover:text-white container'


buttonClasses = 'block rounded w-16 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
acceptClasses = 'block rounded w-16 h-16 m-2 bg-green-600 text-white hover:bg-green-300 focus:outline-white hover:text-gray-800'
rejectClasses = 'block rounded w-16 h-16 m-2 bg-red-600 text-white hover:bg-red-300 focus:outline-white hover:text-gray-800'
actionButtonClasses = 'block rounded w-32 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'

#Codice della grafica della schermata di LOG
############################################
#Prima di tutto, creo un'istanza della classe Agente
ag = agent.Agente()

class FilterScreen:
    def filterScreen(self):
        wp = jp.WebPage()
        wp.body_style='overflow:hidden'
        listaAgenti = ag.getListaAgenti()
        mainDiv = jp.Div(a=wp,classes='box-content bg-gray-700 h-screen border-4 w-screen flex')
        ####### -------> Pulsantiera Sinistra
        subNavDiv = jp.Div(a=mainDiv,classes='h-64 inline-block left-0')
        #- icona per il tasto V -#
        rejectButton = jp.A(href='/log', a=subNavDiv, classes=rejectClasses)
        #rejectButton = jp.Button(a=subNavDiv, classes=rejectClasses)
        rejectIcon = jp.Svg(a=rejectButton, viewBox='0 -2 16 20', xmlns='http://www.w3.org/2000/svg', classes='bi bi-x-lg', fill='currentColor',width='64',height='64')
        rejectPath = jp.Path(a=rejectIcon, d='M1.293 1.293a1 1 0 0 1 1.414 0L8 6.586l5.293-5.293a1 1 0 1 1 1.414 1.414L9.414 8l5.293 5.293a1 1 0 0 1-1.414 1.414L8 9.414l-5.293 5.293a1 1 0 0 1-1.414-1.414L6.586 8 1.293 2.707a1 1 0 0 1 0-1.414z')
        ####### -------> Fine Pulsantiera Sinistra
        ####### -------> Parte Centrale: Log
        #Frame dei bottoni
        frameDiv = jp.Div(a=mainDiv, classes='inline-block w-full h-full overflow-hidden')
        subFrameDiv = jp.Div(a=frameDiv, classes='mt-2 h-full space-y-4')
        #Parte superiore: Titolo
        titleFrameDiv = jp.Div(a=subFrameDiv, classes='block h-16 w-full pt-4')
        spanTitleFrame = jp.Span(a=titleFrameDiv, classes='align-middle')
        jp.P(a=spanTitleFrame, classes='text-center font-black text-3xl subpixel-antialiased text-white', text='Imposta Filtro')
        #Parte centrale: Lista degli agenti                                           
        agentsFrameDiv = jp.Div(a=subFrameDiv,style=f'height:80%; width:100%;', classes='block w-full bg-blue-900 overflow-y-scroll p-2 border-2 border-white rounded-md flex flex-wrap justify-center content-start')
        #jp.P(a=agentsFrameDiv, classes='subpixel-antialiased text-white break-words', text='> '+timestamp+' | '+message+' | '+nomeAgente)
        # Al posto di questo jp.P, bisogna mettere la lista degli agenti che si trova all'interno della finestra.
        for agente in listaAgenti:
            x = jp.Button(a=agentsFrameDiv, classes=agentiClasses, text=agente, mouseenter=self.filtroAgEntra, mouseleave=self.filtroAgEsce, chiave=agente)

        #Pulsantiera delle azioni del log
        actionStartDiv = jp.Div(a=subFrameDiv, classes='block h-16 w-full')
        bottoniStartDiv = jp.Div(a=actionStartDiv, classes='block flex justify-around')
        resetFilterButton = jp.Button(text='Pulisci Filtro', a=bottoniStartDiv, classes=actionButtonClasses)
        #Eventuale altra fila di bottoni
        ####### -------> Fine Parte Centrale: Log
        ####### -------> Parte Destra: Tasto Filtro
        #Menu Destro (Tasto di 'partenza')
        dxButtonsDiv = jp.Div(a=mainDiv,classes='h-64 inline-block w-22') #Aumento la width così da sistemare al meglio la posizione dei bottoni
        #bottone reject al lato destro (X)
        #<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x-lg" viewBox="0 0 16 16">
        #  <path d="M1.293 1.293a1 1 0 0 1 1.414 0L8 6.586l5.293-5.293a1 1 0 1 1 1.414 1.414L9.414 8l5.293 5.293a1 1 0 0 1-1.414 1.414L8 9.414l-5.293 5.293a1 1 0 0 1-1.414-1.414L6.586 8 1.293 2.707a1 1 0 0 1 0-1.414z"/>
        #</svg>
        acceptButton = jp.Button(a=dxButtonsDiv, classes=acceptClasses)
        acceptIcon = jp.Svg(a=acceptButton,viewBox='0 -2 16 20', xmlns='http://www.w3.org/2000/svg', classes='bi bi-check-lg', fill='currentColor',width='64',height='64')
        pathAcceptIcon = jp.Path(d='M13.485 1.431a1.473 1.473 0 0 1 2.104 2.062l-7.84 9.801a1.473 1.473 0 0 1-2.12.04L.431 8.138a1.473 1.473 0 0 1 2.084-2.083l4.111 4.112 6.82-8.69a.486.486 0 0 1 .04-.045z', a=acceptIcon)
        #da cancellare
        #rejectButton = jp.Button(a=dxButtonsDiv, classes=buttonClasses)
        #rejectIcon = jp.Svg(a=rejectButton, viewBox='0 -2 16 20', xmlns='http://www.w3.org/2000/svg', classes='bi bi-x-lg', fill='currentColor',width='64',height='64')
        #rejectPath = jp.Path(a=rejectIcon, d='M1.293 1.293a1 1 0 0 1 1.414 0L8 6.586l5.293-5.293a1 1 0 1 1 1.414 1.414L9.414 8l5.293 5.293a1 1 0 0 1-1.414 1.414L8 9.414l-5.293 5.293a1 1 0 0 1-1.414-1.414L6.586 8 1.293 2.707a1 1 0 0 1 0-1.414z')
        ####### -------> Fine Parte Destra: Tasto Filtro
        return wp

    
    #Lista di Eventi
    def onClickRimuovi(self,msg):
        print('rimuovi agente da filtro')
        #Devo cambiare l'icona in quella di PLAY
        #listaAgenti[msg.target.chiave][3] = False
        ag.setFiltroAgente(msg.target.chiave,False)
        #Primo Step: Cancello tutti i Path
        for element in msg.target.components:
            #print(element)
            msg.target.components.remove(element)
        #Secondo Step: Cambio le componenti del SVG
        msg.target.classes='bi bi-dash-plus-fill'
        msg.target.remove_event('click')
        
        msg.target.on('click',self.onClickAggiungi)
        #Terzo Step: Inserisco l'icona di PIU
        jp.Path(a=msg.target, d='M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.5 4.5a.5.5 0 0 0-1 0v3h-3a.5.5 0 0 0 0 1h3v3a.5.5 0 0 0 1 0v-3h3a.5.5 0 0 0 0-1h-3v-3z')
        
    def onClickAggiungi(self,msg):
        print('aggiungi agente da filtro')
        #listaAgenti[msg.target.chiave][3] = True
        ag.setFiltroAgente(msg.target.chiave,True)
        for element in msg.target.components:
            msg.target.components.remove(element)
        #Secondo Step: Cambio le componenti del SVG
        msg.target.classes='bi bi-dash-circle-fill'
        msg.target.remove_event('click')
        msg.target.on('click',self.onClickRimuovi)
        #Terzo Step: Inserisco l'icona di Meno
        jp.Path(a=msg.target, d='M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM4.5 7.5a.5.5 0 0 0 0 1h7a.5.5 0 0 0 0-1h-7z')
        print('fine creazione path')

    def filtroAgEntra(self,msg):
        print('entra in filtro')
        msg.target.text=''
        msg.target.classes=agentiOnMouseOver

        tastoDiv = jp.Div(a=msg.target, classes='block flex justify-evenly items-center py-3')
            # Play sulla Sinitra
        divPlay = jp.Div(a=tastoDiv, classes='flex-auto')
        #if listaAgenti.get(agente)[1]:
        #       print("prova")
        
        #print('Questo agente fa parte del filtro -->   ' , listaAgenti.get(msg.target.chiave)[3])
        #if listaAgenti.get(msg.target.chiave)[3]:
        #listaAgenti = Agente.getListaAgenti()
        print('PROVA::::: --------> MSG')
        #print(msg)
        #print(msg.target.chiave)
        print(ag.getAgente(msg.target.chiave))
        print(ag.getAgente(msg.target.chiave)[3])
        print(ag.getFiltroAgente(msg.target.chiave))
        print('---------------------')
        if ag.getFiltroAgente(msg.target.chiave):
            #Metti il MENO
            tastoRimuovi = jp.Svg(a=divPlay, xmlns='http://www.w3.org/2000/svg', viewBox='0 0 16 16', width='58', height='40', fill='currentColor', classes='bi bi-dash-circle-fill',mouseenter=self.onIcona, mouseleave=self.leaveIcona, click=self.onClickRimuovi, chiave=msg.target.chiave)
            jp.Path(a=tastoRimuovi, d='M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM4.5 7.5a.5.5 0 0 0 0 1h7a.5.5 0 0 0 0-1h-7z')
            
        else:
            #Metti il PIU
            tastoAggiungi = jp.Svg(a=divPlay, xmlns='http://www.w3.org/2000/svg', viewBox='0 0 16 16', width='58', height='40', fill='currentColor', classes='bi bi-plus-circle-fill',mouseenter=self.onIcona, mouseleave=self.leaveIcona, click=self.onClickAggiungi, chiave=msg.target.chiave)
            jp.Path(a=tastoAggiungi, d='M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM8.5 4.5a.5.5 0 0 0-1 0v3h-3a.5.5 0 0 0 0 1h3v3a.5.5 0 0 0 1 0v-3h3a.5.5 0 0 0 0-1h-3v-3z')
            
            # Code sulla destra
        divCode = jp.Div(a=tastoDiv, classes='flex-auto')
        tastoCode = jp.Input(type='color', a=divCode, classes='', style='width: 40px; height: 40px', input=self.cambioColore, debounce=30)
        #tastoCode = jp.Svg(a=divCode, xmlns='http://www.w3.org/2000/svg', viewBox='0 0 16 16', width='58', height='34', fill='currentColor', classes='bi bi-eyedropper')
        #jp.Path(a=tastoCode, d='M13.354.646a1.207 1.207 0 0 0-1.708 0L8.5 3.793l-.646-.647a.5.5 0 1 0-.708.708L8.293 5l-7.147 7.146A.5.5 0 0 0 1 12.5v1.793l-.854.853a.5.5 0 1 0 .708.707L1.707 15H3.5a.5.5 0 0 0 .354-.146L11 7.707l1.146 1.147a.5.5 0 0 0 .708-.708l-.647-.646 3.147-3.146a1.207 1.207 0 0 0 0-1.708l-2-2zM2 12.707l7-7L10.293 7l-7 7H2v-1.293z')

    def cambioColore(self,msg):
        print('provo a cambiare colore: ')
        print(msg.target.value)
        print('Fine cambio colore')
    def filtroAgEsce(self,msg):
        
        for element in msg.target.components:
            #print(element)
            msg.target.components.remove(element)
        
        msg.target.classes=agentiClasses
        msg.target.mouseenter=self.filtroAgEntra
        msg.target.mouseleave=self.filtroAgEsce
        msg.target.text=msg.target.chiave
        #print('USCITO')

    def showAgentButtons(self):
        print('prova')
    
    def onIcona(self, msg):
        print('tocco icona')
        msg.target.fill='red'
        #print(msg.target.components[0].d)

    def leaveIcona(self,msg):
        print('esco icona')
        msg.target.fill='currentColor'
