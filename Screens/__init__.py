#!/usr/bin/python
# This Python file uses the following encoding: utf-8
'''
@author: Federico Tersigni
'''

import justpy as jp

#Variabili output: per ora solo prove
timestamp = 'TimeStamp'
message = 'Message'
nomeAgente = 'Nome Agente'

#legato a start
listaAgenti = ['x','y','z','t','u','x','y','z','t','u','x','y','z','t','u']


#Costanti delle Classi / Tailwind dei bottoni
agentiClasses = 'inline-block rounded w-32 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
agentiOnMouseOver = 'inline-block rounded w-32 h-16 bg-blue-600 m-2 text-white hover:bg-blue-400 focus:outline-white hover:text-white container'


buttonClasses = 'block rounded w-16 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
acceptClasses = 'block rounded w-16 h-16 m-2 bg-green-600 text-white hover:bg-green-300 focus:outline-white hover:text-gray-800'
rejectClasses = 'block rounded w-16 h-16 m-2 bg-red-600 text-white hover:bg-red-300 focus:outline-white hover:text-gray-800'
actionButtonClasses = 'block rounded w-32 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'

#Codice della grafica della schermata di LOG
############################################


class Screen:
    #Le impostazioni settate dal config screen dovrebbero poter modificare le variabili che contengono il nome delle classi (per esempio agentiClasses)

    def debugScreen(self):
        print('Legge questa funzione')
        pass
    
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


    ##################################################################################################################################################################################
    # Eventi del mouse comuni per ogni icona
    def onIcona(self, msg):
        print('tocco icona')
        msg.target.fill='red'
    def leaveIcona(self,msg):
        print('esco icona')
        msg.target.fill='currentColor'

    # Eventi click che richiama la funzione corrispondente
    def onClickCode(self,msg):
        print('Apre il codice sorgente dell agente selezionato')

    def onClickPlay(self, msg):
        print('Agente Attivato')
        #Devo cambiare l'icona in quella di STOP
    
    def onClickStop(self, msg):
        print('Agente Disattivato')
        #Devo cambiare l'icona in quella di PLAY



    #prova EVENTI -- Prova a inserire altri eventi negli elementi aggiunti da 'agEntra' per vedere la loro efficacia
    def agEntra(self,msg): 
        #Quando il cursore entra nel bottone, vengono visualizzate le due icone inerenti a quel determinato agente
        #Entra nel bottone
        #print(msg.target.events)
        #print(msg.target.has_event_function('mouseleave'))
        msg.target.text=''
        msg.target.classes=agentiOnMouseOver

        tastoDiv = jp.Div(a=msg.target, classes='block flex justify-evenly items-center py-3')
            # Play sulla Sinitra
        divPlay = jp.Div(a=tastoDiv, classes='flex-auto')
        tastoPlay = jp.Svg(a=divPlay, xmlns='http://www.w3.org/2000/svg', viewBox='0 0 16 16', width='58', height='40', fill='currentColor', classes='bi bi-play-fill',mouseenter=self.onIcona, mouseleave=self.leaveIcona)
        jp.Path(a=tastoPlay, d='m11.596 8.697-6.363 3.692c-.54.313-1.233-.066-1.233-.697V4.308c0-.63.692-1.01 1.233-.696l6.363 3.692a.802.802 0 0 1 0 1.393z')
            
            
            # Code sulla destra
        divCode = jp.Div(a=tastoDiv, classes='flex-auto')
        tastoCode = jp.Svg(a=divCode, xmlns='http://www.w3.org/2000/svg', viewBox='0 0 16 16', width='58', height='34', fill='currentColor', classes='bi bi-code-square')
        jp.Path(a=tastoCode, d='M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z')
        jp.Path(a=tastoCode, d='M6.854 4.646a.5.5 0 0 1 0 .708L4.207 8l2.647 2.646a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 0 1 .708 0zm2.292 0a.5.5 0 0 0 0 .708L11.793 8l-2.647 2.646a.5.5 0 0 0 .708.708l3-3a.5.5 0 0 0 0-.708l-3-3a.5.5 0 0 0-.708 0z')

            #Ogni bottone ha un suo specifico evento (MouseEnter per il cambio colore, Click per il trigger della funzione corrispondente)
        


        #print('ENTRATO ' + msg.target.nome)
    
    def agEsce(self,msg):
        #print('###')
        #print(self.text)
        #self.text='Uscito'
        #self.set_class='bg-red-200'
        #print(msg.target)
        #print(msg.target)

        #print('disegno bottone')
        for element in msg.target.components:
            #print(element)
            msg.target.components.remove(element)
        #msg.target.remove_event('mouseleave')

        #print('setto il suo stato iniziale')
        #print(msg.target.events)
        #print(msg.target.has_event_function('mouseleave'))
        msg.target.classes=agentiClasses
        msg.target.mouseenter=self.agEntra
        msg.target.mouseleave=self.agEsce
        msg.target.text=msg.target.nome
        #print('USCITO')
    
    
    #Codice della schermata di Start

    def startScreen(self):
        wp = jp.WebPage()
        wp.body_style='overflow:hidden'
        mainDiv = jp.Div(a=wp,classes='box-content bg-gray-700 h-screen border-4 w-screen flex')
        
        ####### -------> Pulsantiera Sinistra

        subNavDiv = jp.Div(a=mainDiv,classes='h-64 inline-block left-0')

        #- icona per il tasto del menu start -# IN QUESTO CASO, QUESTO BOTTONE E' DISABLED
        initButtonNav = jp.Button(a=subNavDiv, classes=buttonClasses)
        menuStartIcon = jp.Svg(a=initButtonNav,viewBox='0 -2 16 20', xmlns='http://www.w3.org/2000/svg', classes='bi bi-play-circle', fill='currentColor',width='64',height='64')
        pathStartIconA = jp.Path(d='M8 15A7 7 0 1 1 8 1a7 7 0 0 1 0 14zm0 1A8 8 0 1 0 8 0a8 8 0 0 0 0 16z', a=menuStartIcon)
        pathStartIconB = jp.Path(d='M6.271 5.055a.5.5 0 0 1 .52.038l3.5 2.5a.5.5 0 0 1 0 .814l-3.5 2.5A.5.5 0 0 1 6 10.5v-5a.5.5 0 0 1 .271-.445z', a=menuStartIcon)
        #- icona per il tasto del menu log -#
        logButtonNav = jp.A(href='/log', a=subNavDiv, classes=buttonClasses)
        #logButtonNav = jp.Button(a=subNavDiv, classes=buttonClasses)
        logIcon = jp.Svg(a=logButtonNav, viewBox='0 -2 16 20', xmlns='http://www.w3.org/2000/svg', classes='bi bi-chat-right-text', fill='currentColor',width='64',height='64')
        logIconPathA = jp.Path(d='M2 1a1 1 0 0 0-1 1v8a1 1 0 0 0 1 1h9.586a2 2 0 0 1 1.414.586l2 2V2a1 1 0 0 0-1-1H2zm12-1a2 2 0 0 1 2 2v12.793a.5.5 0 0 1-.854.353l-2.853-2.853a1 1 0 0 0-.707-.293H2a2 2 0 0 1-2-2V2a2 2 0 0 1 2-2h12z',a=logIcon)
        logIconPathB = jp.Path(d='M3 3.5a.5.5 0 0 1 .5-.5h9a.5.5 0 0 1 0 1h-9a.5.5 0 0 1-.5-.5zM3 6a.5.5 0 0 1 .5-.5h9a.5.5 0 0 1 0 1h-9A.5.5 0 0 1 3 6zm0 2.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1h-5a.5.5 0 0 1-.5-.5z',a=logIcon)
        #- icona per il tasto di configurazione -#
        configButtonNav = jp.Button(a=subNavDiv, classes=buttonClasses)
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
        jp.P(a=spanTitleFrame, classes='text-center font-black text-3xl subpixel-antialiased text-white', text='Schermata di Start')

        #Parte centrale: Lista degli agenti                                           
        agentsFrameDiv = jp.Div(a=subFrameDiv,style=f'height:80%; width:100%;', classes='block w-full bg-blue-900 overflow-y-scroll p-2 border-2 border-white rounded-md flex flex-wrap justify-center content-start')
        #jp.P(a=agentsFrameDiv, classes='subpixel-antialiased text-white break-words', text='> '+timestamp+' | '+message+' | '+nomeAgente)
        # Al posto di questo jp.P, bisogna mettere la lista degli agenti che si trova all'interno della finestra.

        for agente in listaAgenti:
            #Inizio Prova
            x = jp.Div(a=agentsFrameDiv, classes=agentiClasses, text='nomeAgente', mouseenter=self.agEntra, mouseleave=self.agEsce, nome='nomeAgente')
            
            #Fine Prova
            # 1) Non appena viene disegnato, dovrà mostrare il nome dell'agente
            # 2) Se ci passa il mouse, cambia e mostra il suo secondo aspetto
            # 3) Non appena il mouse esce dall'area, l'agente ritorna nel primo stato


            #jp.Button(a=agentsFrameDiv, classes=agentiClasses, text='nomeAgente')
            #tastoAgente = jp.Div(a=agentsFrameDiv, classes=agentiOnMouseOver) #, text='nomeAgente')
            #tastoDiv = jp.Div(a=tastoAgente, classes='block flex justify-evenly items-center py-3')
            # Play sulla Sinitra
            #divPlay = jp.Div(a=tastoDiv, classes='flex-auto')
            #tastoPlay = jp.Svg(a=divPlay, xmlns='http://www.w3.org/2000/svg', viewBox='0 0 16 16', width='58', height='40', fill='currentColor', classes='bi bi-play-fill')
            #jp.Path(a=tastoPlay, d='m11.596 8.697-6.363 3.692c-.54.313-1.233-.066-1.233-.697V4.308c0-.63.692-1.01 1.233-.696l6.363 3.692a.802.802 0 0 1 0 1.393z')
            
            
            # Code sulla destra
            #divCode = jp.Div(a=tastoDiv, classes='flex-auto')
            #tastoCode = jp.Svg(a=divCode, xmlns='http://www.w3.org/2000/svg', viewBox='0 0 16 16', width='58', height='34', fill='currentColor', classes='bi bi-code-square')
            #jp.Path(a=tastoCode, d='M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z')
            #jp.Path(a=tastoCode, d='M6.854 4.646a.5.5 0 0 1 0 .708L4.207 8l2.647 2.646a.5.5 0 0 1-.708.708l-3-3a.5.5 0 0 1 0-.708l3-3a.5.5 0 0 1 .708 0zm2.292 0a.5.5 0 0 0 0 .708L11.793 8l-2.647 2.646a.5.5 0 0 0 .708.708l3-3a.5.5 0 0 0 0-.708l-3-3a.5.5 0 0 0-.708 0z')

            #Ogni bottone ha un suo specifico evento (MouseEnter per il cambio colore, Click per il trigger della funzione corrispondente)



        #Pulsantiera delle azioni del log
        actionStartDiv = jp.Div(a=subFrameDiv, classes='block h-16 w-full')
        bottoniStartDiv = jp.Div(a=actionStartDiv, classes='block flex justify-around')
        addAgentButton = jp.Button(text='Aggiungi Agente', a=bottoniStartDiv, classes=actionButtonClasses)
        removeAgentButton = jp.Button(text='Rimuovi Agente', a=bottoniStartDiv, classes=actionButtonClasses)

        #Eventuale altra fila di bottoni
        ####### -------> Fine Parte Centrale: Log

        ####### -------> Parte Destra: Tasto Filtro

        #Menu Destro (Tasto di 'partenza')
        dxButtonsDiv = jp.Div(a=mainDiv,classes='h-64 inline-block w-22') #Aumento la width così da sistemare al meglio la posizione dei bottoni
        #Bottone destro
        powerOnButton = jp.Button(a=dxButtonsDiv, classes=buttonClasses)
        powerOnIcon = jp.Svg(a=powerOnButton, viewBox='0 -2 16 20', xmlns='http://www.w3.org/2000/svg', classes='bi bi-power', fill='currentColor',width='64',height='64')
        powerPathA = jp.Path(a=powerOnIcon, d='M7.5 1v7h1V1h-1z')
        powerPathB = jp.Path(a=powerOnIcon, d='M3 8.812a4.999 4.999 0 0 1 2.578-4.375l-.485-.874A6 6 0 1 0 11 3.616l-.501.865A5 5 0 1 1 3 8.812z')
        ####### -------> Fine Parte Destra: Tasto Filtro

        return wp


    ##########################################################
    #Codice Schermata di configurazione

    def filterScreen(self):
        wp = jp.WebPage()
        wp.body_style='overflow:hidden'
        mainDiv = jp.Div(a=wp,classes='box-content bg-gray-700 h-screen border-4 w-screen flex')
        
        ####### -------> Pulsantiera Sinistra

        subNavDiv = jp.Div(a=mainDiv,classes='h-64 inline-block left-0')

        #- icona per il tasto V -#
        rejectButton = jp.A(href='/log', a=subNavDiv, classes=rejectClasses)
        #rejectButton = jp.Button(a=subNavDiv, classes=rejectClasses)
        rejectIcon = jp.Svg(a=rejectButton, viewBox='0 -2 16 20', xmlns='http://www.w3.org/2000/svg', classes='bi bi-x-lg', fill='currentColor',width='64',height='64')
        rejectPath = jp.Path(a=rejectIcon, d='M1.293 1.293a1 1 0 0 1 1.414 0L8 6.586l5.293-5.293a1 1 0 1 1 1.414 1.414L9.414 8l5.293 5.293a1 1 0 0 1-1.414 1.414L8 9.414l-5.293 5.293a1 1 0 0 1-1.414-1.414L6.586 8 1.293 2.707a1 1 0 0 1 0-1.414z')


        #da cancellare
        #acceptButton = jp.Button(a=subNavDiv, classes=buttonClasses)
        #acceptIcon = jp.Svg(a=acceptButton,viewBox='0 -2 16 20', xmlns='http://www.w3.org/2000/svg', classes='bi bi-check-lg', fill='currentColor',width='64',height='64')
        #pathAcceptIcon = jp.Path(d='M13.485 1.431a1.473 1.473 0 0 1 2.104 2.062l-7.84 9.801a1.473 1.473 0 0 1-2.12.04L.431 8.138a1.473 1.473 0 0 1 2.084-2.083l4.111 4.112 6.82-8.69a.486.486 0 0 1 .04-.045z', a=acceptIcon)
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
            jp.Button(a=agentsFrameDiv, classes=agentiClasses, text='nomeAgente')



        #Pulsantiera delle azioni del log
        actionStartDiv = jp.Div(a=subFrameDiv, classes='block h-16 w-full')
        bottoniStartDiv = jp.Div(a=actionStartDiv, classes='block flex justify-around')
        #addAgentButton = jp.Button(text='Aggiungi Agente', a=bottoniStartDiv, classes=actionButtonClasses)
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

#jp.justpy(html_compo)
    
    #Lista di Eventi

    def showAgentButtons(self):
        print('prova')
        