from Esercizio import Esercizio
from typing import List

class Verifica:
    

    def __init__(
            self,
            n_esercizi : int = 1,
            
    ):
        self.n_esercizi = n_esercizi
        es = Esercizio()
        self.esercizi : List[Esercizio] = [es.copy() for _ in range(n_esercizi)]

    def aggiungi_esercizio(
            self,
            ex: Esercizio,
    ):
        for es in self.esercizi:
            if es == Esercizio():
                es = ex
            
    def stampa(self):
        print(self.esercizi[0].testo)

