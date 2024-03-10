from Esercizio import Esercizio
from typing import List

class Verifica:
    """
        Classe Verifica, 
        variabile: 
                n_esercizi : numero esercizi, 
                esercizi : una lista di elementi della classe Esercizio di dimensioni n_esercizi
    """

    def __init__(
            self,
            n_esercizi : int = 1,            
    ):
        """
        Inizializza una nuova Verifica con il numero specificato di esercizi.

        Args:
            n_esercizi (int, optional): Il numero totale di esercizi nella verifica. Default è 1.
        """
        self.n_esercizi = n_esercizi
        es = Esercizio()
        self.esercizi : List[Esercizio] = [es.copy() for _ in range(n_esercizi)]

    def Aggiungi_esercizio(
            self, 
            ex: Esercizio
            ):
        """
        Aggiunge un nuovo esercizio alla verifica.

        Trova il primo elemento non inizializzato e sostituiscilo con l'esercizio dato in input.

        Args:
            ex (Esercizio): L'esercizio da aggiungere alla verifica.
        """
        for i, es in enumerate(self.esercizi):
            if self.esercizio_std(es):
                self.esercizi[i] = ex
                return


    def esercizio_std(self, es: Esercizio):
        """
        Verifica se un esercizio è standard, ossia se tutti i suoi campi sono vuoti o impostati ai valori predefiniti.

        Args:
            es (Esercizio): L'esercizio da verificare.

        Returns:
            bool: True se l'esercizio è standard, False altrimenti.
        """
        return (
            es.tematica == "" and
            es.testo == "" and
            es.argomento.oda == "" and
            es.argomento.sottotematica == "" and
            es.argomento.trasversalita == False and
            es.argomento.centralita == 1 and
            es.difficolta.dsa == False and
            es.difficolta.tipologia == "esercizio" and
            es.difficolta.infamia == 0 and
            es.difficolta.livello == "base" and
            es.materia == "" and
            es.risposta == ""
        )

