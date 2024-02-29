import tkinter as tk

from Esercizio import Esercizio
from Finestra_caricamento import Finestra_caricamento
from Finestra_generazione import Finestra_generazione
from Tkinter_methods import Chiudi_finestra
def Finestra_home():
    """
    Apre una finestra principale per il programma,
    Permette di scegliere tra la generazione di una verifica e il caricamento di un esercizio.

    Returns:
        None
    """
    home = tk.Tk()

    home.title("home")
    home.geometry('500x400')

    message = tk.Label(home, compound=tk.CENTER, bg="yellow", text="Cosa vuoi fare?" )
    message.pack()

    

    def Chiama_generazione():
        """
        Chiude la finestra principale e apre la finestra per la generazione di una verifica.

        Returns:
            None
        """
        Chiudi_finestra(home)
        Finestra_generazione()

    def Chiama_caricamento():
        """
        Chiude la finestra principale e apre la finestra per il caricamento di un esercizio su un file json.

        Returns:
            None
        """
        Chiudi_finestra(home)
        es = Esercizio()
        Finestra_caricamento(es)

    genera = tk.Button(home, bg="orange", text="Genera una verifica", command=Chiama_generazione)
    genera.pack()

    carica = tk.Button(home, bg="light green", text="Carica un esercizio", command=Chiama_caricamento)
    carica.pack()

    home.mainloop()

