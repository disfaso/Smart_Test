from Esercizio import Esercizio

class Verifica:
    

    def __init__(
            self,
            n_esercizi : int = 1,
            
    ):
        self.n_esercizi = n_esercizi
        es = Esercizio()
        self.esercizi : Esercizio = [es] * n_esercizi

    def aggiungi_esercizio(
            self,
            ex: Esercizio,
    ):
        for es in self.esercizi:
            if es == Esercizio():
                es = ex
            

