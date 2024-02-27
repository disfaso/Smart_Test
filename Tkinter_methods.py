from tkinter import messagebox
from Esercizio import Esercizio

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)

def Valida_input(testo):
    if testo.isdigit() or testo == "":
        return True
    else:
        messagebox.showerror("Error", "Si prega di inserire esclusivamente valori numerici")
        return False
    

def Valori_esercizio(ex: Esercizio,
                     tematica,
                     testo,
                     oda,
                     sottotematica,
                     trasversalita,
                     centralita,
                     dsa,
                     tipologia,
                     infamia,
                     livello,
                     materia,
                     risposta
                     ):
    ex.materia = materia.get()
    ex.risposta = risposta.get()
    ex.tematica = tematica.get()
    ex.testo = testo.get()
    ex.argomento.oda = oda.get()
    ex.argomento.sottotematica = sottotematica.get()
    ex.argomento.trasversalita = trasversalita.get()
    ex.argomento.centralita = centralita.get()
    ex.difficolta.dsa = dsa.get()
    ex.difficolta.tipologia = tipologia.get()
    ex.difficolta.infamia = infamia.get()
    ex.difficolta.livello = livello.get()