class Argomento:
    def __init__(
        self, 
        oda = "", 
        sottotematica = "", 
        trasversalità: bool = False, 
        centralità = 1
        ):
        self.oda = oda
        self.sottotematica = sottotematica
        self.trasversalità = trasversalità
        self.centralità = centralità

class Difficoltà:
    def __init__(
            self, 
            dsa = 0,
            tipologia = "esercizio",
            infamia = 0,
            livello = "base"
    ):
        self.dsa = dsa
        self.tipologia = tipologia
        self.infamia = infamia
        self.livello = livello


class Esercizio:
    def __init__(self, 
                 tematica = "", 
                 testo = "", 
                 argomento= Argomento(), 
                 difficoltà = Difficoltà(), 
                 materia = "", 
                 risposta = ""):
        self.tematica = tematica
        self.testo = testo
        self.argomento = argomento
        self.difficoltà = difficoltà
        self.materia = materia
        self.risposta = risposta

    
        