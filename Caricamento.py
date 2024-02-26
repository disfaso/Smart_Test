import tkinter as tk
from Finestra_caricamento import Finestra_caricamento
from Esercizio import Esercizio
#def drag_start(event):
#    widget = event.widget
#    widget.startX = event.x
 #   widget.startY = event.y

#def drag_motion(event):
 #   widget = event.widget
  #  x = widget.winfo_x() - widget.startX + event.x
   # y = widget.winfo_y() - widget.startY + event.y
    #widget.place(x=x, y=y)




def Carica():
    esercizio = Esercizio()
    Finestra_caricamento(esercizio)




