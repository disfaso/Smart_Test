import tkinter as tk
from Esercizio import Esercizio

def Finestra_caricamento(es: Esercizio):
    caricamento = tk.Tk()

    caricamento.title("Carica un esercizio")
    caricamento.geometry('1000x800')

#instruzioni per il caricamento
    message = tk.Label(caricamento, compound=tk.CENTER, bg="yellow", text="Trascina qui l'esercizio")
    message.grid(row=0, column=3)

#Tematica
    tematica = tk.Label(caricamento, bg="light green", text="Inserire l'unità di apprendimento dell'esercizio")    
    tematica.grid(row=1, column=0)

    tematica_in = tk.Entry(caricamento, validate="key")
    tematica_in.grid(row=1, column=1)

#Testo
    testo = tk.Label(caricamento, bg="light green", text="Inserire il testo dell'esercizio")    
    testo.grid(row=2, column=0)

    testo_in = tk.Entry(caricamento, validate="key")
    testo_in.grid(row=2, column=1)

#Argomento
    #oda
    oda = tk.Label(caricamento, bg="light green", text="Inserire gli obiettivi di apprendimento dell'esercizio")    
    oda.grid(row=3, column=0)

    oda_in = tk.Entry(caricamento, validate="key")
    oda_in.grid(row=3, column=1)

    #sottotematica
    sottotematica = tk.Label(caricamento, bg="light green", text="Inserire la sottotematica dell'esercizio")    
    sottotematica.grid(row=4, column=0)

    sottotematica_in = tk.Entry(caricamento, validate="key")
    sottotematica_in.grid(row=4, column=1)

    print("sottotematica: ", sottotematica_in.get())

    #trasversalità
    trasversalità = tk.Checkbutton(caricamento, background = "light green", text="L'esercizio ha trasversalità per più materie?", variable= es.argomento.trasversalità)
    trasversalità.grid(row=5, column=0)
    print("trasversalità: ", trasversalità)

    #centralità
    centralità = tk.Label(caricamento, bg="light green", text="Inserire la centralità dell'esercizio alla sua sottotematica")    
    centralità.grid(row=6, column=0)

    centralità_in = tk.Entry(caricamento, validate="key")
    centralità_in.grid(row=6, column=1)
    

#Difficoltà
    #tipologia
    tipologia = tk.Label(caricamento, bg="light green", text="Scegliere la tipologia dell'esercizio")    
    tipologia.grid(row=7, column=0)

    tipologie = ["teoria", "definizione", "problema", "esercizio"]
    selezionata = tk.StringVar()
    selezionata.set(tipologie[3])
    tipologia_in = tk.OptionMenu(caricamento, selezionata, *tipologie)
    tipologia_in.grid(row=7, column = 1)

    
#bottone per fissare i valori alla variabile esercizio e chiamare il json
  #  get_value_button = tk.Button(caricamento, text="Carica l'esercizio", command=Genera_esercizio)
   # get_value_button.grid(row=10, column=4)
    
   # get_option_button = tk.Button(root, text="Get Option", command=option_selected)
#    get_option_button.pack(pady=5)
   # message.bind("<Button-1>", drag_start)
   # message.bind("<B1-Motion>", drag_motion)

    caricamento.mainloop()