#!/usr/bin/python
# This Python file uses the following encoding: utf-8
'''
@author: Federico Tersigni
'''

import justpy as jp
import os
import sys

#handlerAgenti avrà le funzioni di salvataggio e apertura del codice dell'agente specifico

from Template.EditorAgenteView import EditorAgenteView


from Screens.Sessione import esisteSessione
from Screens.Sessione import creaSessione
from Screens.Sessione import showSessione
from Screens.Sessione import utenteLoggato
from Screens.Sessione import returnSessione
from Screens.Sessione import esisteChiave
from Screens.Sessione import returnElemento
from Screens.Sessione import addElementoSessione
from Screens.Sessione import cambiaAttributoAgente


#Costanti delle Classi / Tailwind dei bottoni
agentiClasses = 'inline-block rounded w-32 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
agentiOnMouseOver = 'inline-block rounded w-32 h-16 bg-blue-600 m-2 text-white hover:bg-blue-400 focus:outline-white hover:text-white container'


buttonClasses = 'block rounded w-16 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
acceptClasses = 'block rounded w-16 h-16 m-2 bg-green-600 text-white hover:bg-green-300 focus:outline-white hover:text-gray-800'
rejectClasses = 'block rounded w-16 h-16 m-2 bg-red-600 text-white hover:bg-red-300 focus:outline-white hover:text-gray-800'
actionButtonClasses = 'block rounded w-32 h-16 m-2 bg-blue-600 text-white hover:bg-white focus:outline-white hover:text-gray-800'
#Codice della grafica della schermata dell'editor


############################################

class EditorAgente:
    nome, path = '',''

    def editorAgente(self,request):
        print('editorAgente')
        s_id = request.session_id

        session = {}
        # Procedura di Sessione
        if not esisteSessione(s_id):
            creaSessione(s_id,False)
        else:
            #METTI TUTTI I DATI NELLE VARIABILI CHE MI SERVONO
            #IF PER VEDERE SE SIAMO LOGGATI O MENO
            if utenteLoggato(s_id):
                session = returnSessione(s_id)
            

            showSessione(s_id)

        chiave = 'path'

        if esisteChiave(s_id, chiave):
            path = returnElemento(s_id, chiave)
            self.path = path

            nomeAgente = {request.path_params["name"]}.pop()
            self.nome = nomeAgente
        else:
            print('errore in EditorAgente - no Path')
            #REDIRECT
        #lunga=self.apriCodice(nomeAgente) 
        codice = self.apriCodice(self.path,self.nome)
        print('dopo funzione apriCodice')
        wp = EditorAgenteView(self.nome,codice,self.salvaCodice)

        return wp
        

    def apriCodice(self,path,nome):
        ## INIZIO LA PROVA
        print('apro codice')
        print(path)
        lunga=''
        ag_path=path+nome #+'.py'
        path = os.path.abspath(ag_path)
        print('--------')
        print(path)
        with open(ag_path,'r') as l:
            Linee = l.readlines()
            
            print(Linee)
            #print('#####', Linee[0])
            for n in Linee:
                lunga = f'{lunga}{n}'
            print(lunga)
        #IL PARSER DEVE: 1) dividere le righe leggendo il codice per mandare a capo /n  
        l.close()
        return lunga

    def salvaCodice(self,msg):
        print('Salva codice')
        content=msg.form_data[0].value
        nome=self.nome
        ag_path=self.path+nome #+'.py'
        path = os.path.abspath(ag_path)
        file_agente=open(path,'w')
        file_agente.write(content)
        file_agente.close()
        
        msg.page.redirect= '/start'

        print('Codice Salvato')