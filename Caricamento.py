import tkinter as tk

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)




def Carica():
    caricamento = tk.Tk()

    caricamento.title("Carica un esercizio")
    caricamento.geometry('1000x800')

    message = tk.Label(caricamento, compound=tk.CENTER, bg="yellow", text="Trascina qui l'esercizio")
    message.place(x=450, y=100)

    message.bind("<Button-1>", drag_start)
    message.bind("<B1-Motion>", drag_motion)

    caricamento.mainloop()




