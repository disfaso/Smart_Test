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
    """
        Inizializza un oggetto Difficolta con i parametri specificati.

        Args:
            dsa (bool): Indica se l'esercizio risulta problematico per studenti con DSA (disturbi specifici dell'apprendimento).
            tipologia (str): Tipologia del quesito: può assumere valori: problema, esercizio, teoria, definizione
            infamia (int): Valore di infamia dell'esercizio.
            livello (str): Livello di difficoltà dell'esercizio, valori possibili: base, medio, avanzato
        """

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
        """
        Inizializza un oggetto Esercizio con i parametri specificati.

        Args:
            tematica (str): Tematica dell'esercizio.
            testo (str): Testo dell'esercizio.
            argomento (Argomento): Oggetto Argomento associato all'esercizio.
            difficolta (Difficolta): Oggetto Difficolta associato all'esercizio.
            materia (str): Materia dell'esercizio.
            risposta (str): Risposta dell'esercizio.
        """
        self.tematica = tematica
        self.testo = testo
        self.argomento = argomento
        self.difficolta = difficolta
        self.materia = materia
        self.risposta = risposta

    def copy(self):
        """
        Crea una copia dell'oggetto Esercizio.

        Returns:
            Esercizio: Una copia dell'oggetto Esercizio.
        """
        return Esercizio(
            tematica=self.tematica,
            testo=self.testo,
            argomento=self.argomento,
            difficolta=self.difficolta,
            materia=self.materia,
            risposta=self.risposta
        )

    
        