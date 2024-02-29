class Argomento:
    """
        Inizializza un oggetto Argomento

        Args:
            oda (str): Descrizione del ODA (Obiettivo di Apprendimento).
            sottotematica (str): Descrizione dell'argomento specifico dell'esercizio'.
            trasversalita (bool): Indica se l'argomento è trasversale.
            centralita (int): Valore di centralità dell'argomento rispetto alla sua unità.
        """
    def __init__(
        self, 
        oda = "", 
        sottotematica = "", 
        trasversalita: bool = False, 
        centralita = 1
        ):
        self.oda = oda
        self.sottotematica = sottotematica
        self.trasversalita = trasversalita
        self.centralita = centralita

class Difficolta:
    def __init__(
            self, 
            dsa = False,
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
                 difficolta = Difficolta(), 
                 materia = "", 
                 risposta = ""):
        self.tematica = tematica
        self.testo = testo
        self.argomento = argomento
        self.difficolta = difficolta
        self.materia = materia
        self.risposta = risposta

    def copy(self):
        """
         Creare una copia di Esercizio
        """
        return Esercizio(
            tematica=self.tematica,
            testo=self.testo,
            argomento=self.argomento,
            difficolta=self.difficolta,
            materia=self.materia,
            risposta=self.risposta
        )

    
        