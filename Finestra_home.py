import tkinter as tk

from Esercizio import Esercizio
from Finestra_caricamento import Finestra_caricamento
from Finestra_generazione import Finestra_generazione
from Tkinter_methods import Chiudi_finestra
def Finestra_home():
    home = tk.Tk()

    home.title("home")
    home.geometry('500x400')

    message = tk.Label(home, compound=tk.CENTER, bg="yellow", text="Cosa vuoi fare?" )
    message.pack()

    

    def Chiama_generazione()
        Chiudi_finestra(home)
        Finestra_generazione()

    def Chiama_caricamento()
        Chiudi_finestra(home)
        es = Esercizio()
        Finestra_caricamento(es)

    genera = tk.Button(home, bg="orange", text="Genera una verifica", command=Chiama_generazione)
    genera.pack()

    carica = tk.Button(home, bg="light green", text="Carica un esercizio", command=Chiama_caricamento)
    carica.pack()

