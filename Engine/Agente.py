listaAgenti = {
# Struttura listaAgenti: "NomeAgente",[URL posizione, Stato attività, Colore, filtrato]
    "Agente_002": ["Posizione",True,"#666666",True],
    "Agente_003": ["Posizione",True,"#6adbad",True],
    "Agente_007": ["Posizione",True,"#aded26",True],
    "Agente_012": ["Posizione",True,"#999999",True],
    "Agente_0993": ["Posizione",True,"#66acdf",True],
    "Agente_Agente 39": ["Posizione",True,"#FFF34b",True],
    "Agent 233": ["Posizione",True,"#666666",True],
    "NomeAgente1": ["Posizione",True,"#ccc666",True],
    "Agente_092age": ["Posizione",True,"#0acc34",True]

}

class Agente:
    def __init__(self):
        pass

    #Probabilmente manca una funzione che, dato un dizionario, sostituisce listaAgenti con questo dizionario (funzione per fare update)

    def getListaAgenti(self):
        return listaAgenti

    def setPosizioneAgente(self,chiave,posizione):
        listaAgenti[chiave][0] = posizione

    def setStatoAgente(self,chiave,stato):
        listaAgenti[chiave][1] = stato

    def setColoreAgente(self,chiave,colore):
        listaAgenti[chiave][2] = colore

    def setFiltroAgente(self,chiave,inFiltro):
        listaAgenti[chiave][3] = inFiltro

    def getAgente(self,chiave):
        return listaAgenti.get(chiave)

    def getPosizioneAgente(self,chiave):
        return listaAgenti.get(chiave)[0]

    def getStatoAgente(self,chiave):
        return listaAgenti.get(chiave)[1]

    def getColoreAgente(self,chiave):
        return listaAgenti.get(chiave)[2]

    def getFiltroAgente(self,chiave):
        return listaAgenti.get(chiave)[3]

    def clearListaAgenti(self):
        listaAgenti.clear()
