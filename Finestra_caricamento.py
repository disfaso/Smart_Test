import tkinter as tk
from Esercizio import Esercizio
from Tkinter_methods import Valori_esercizio
from Carica_esercizio import Creazione_dati
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

    #centralità
    centralità = tk.Label(caricamento, bg="light green", text="Inserire la centralità dell'esercizio alla sua sottotematica")    
    centralità.grid(row=6, column=0)

    centralità_in = tk.Entry(caricamento, validate="key")
    centralità_in.grid(row=6, column=1)
    

#Difficoltà
    #dsa
    dsa = tk.Checkbutton(caricamento, background = "light green", text="L'esercizio presenta difficoltà per chi soffre di disturbi specifici dell'apprendimento?", variable= es.difficoltà.dsa)
    dsa.grid(row=11, column=0)

    #tipologia
    tipologia = tk.Label(caricamento, bg="light green", text="Scegliere la tipologia dell'esercizio")    
    tipologia.grid(row=7, column=0)

    tipologie = ["teoria", "definizione", "problema", "esercizio"]
    tip_selezionata = tk.StringVar()
    tip_selezionata.set(tipologie[3])
    tipologia_in = tk.OptionMenu(caricamento, tip_selezionata, *tipologie)
    tipologia_in.grid(row=7, column = 1)

    #infamia
    infamia = tk.Label(caricamento, bg="light green", text="Scegliere il livello di infamia dell'esercizio")    
    infamia.grid(row=8, column=0)

    lvl_infamia = [1, 2, 3, 4, 5, 666]
    lvl_selezionato = tk.StringVar()
    lvl_selezionato.set(lvl_infamia[2])
    infamia_in = tk.OptionMenu(caricamento, lvl_selezionato, *lvl_infamia)
    infamia_in.grid(row=8, column=1)

    #livello
    livello = tk.Label(caricamento, bg="light green", text="Scegliere il livello dell'esercizio")    
    livello.grid(row=9, column=0)

    livelli = ["base", "medio", "avanzato"]
    selezionato = tk.StringVar()
    selezionato.set(livelli[0])
    livello_in = tk.OptionMenu(caricamento, selezionato, *livelli)
    livello_in.grid(row=9, column=1)

    #materia
    materia = tk.Label(caricamento, bg="light green", text="Inserire la materia a cui appartiene l'esercizio")    
    materia.grid(row=10, column=0)

    materia_in = tk.Entry(caricamento, validate="key")
    materia_in.grid(row=10, column=1)

    #risposta
    risposta = tk.Label(caricamento, bg="light green", text="Inserire la risposta dell'esercizio")    
    risposta.grid(row=10, column=0)

    risposta_in = tk.Entry(caricamento, validate="key")
    risposta_in.grid(row=10, column=1)

    def Bottone_carica():
        Valori_esercizio(es, 
                         tematica_in, 
                         testo_in, 
                         oda_in, 
                         sottotematica_in, 
                         es.argomento.trasversalità, 
                         centralità_in, 
                         es.difficoltà.dsa, 
                         tip_selezionata, 
                         lvl_selezionato, 
                         selezionato, 
                         materia_in, 
                         risposta_in)
        Creazione_dati(es=es)

#bottone per fissare i valori alla variabile esercizio e chiamare il json
    valori_esercizio = tk.Button(caricamento, text="Carica l'esercizio", command=Bottone_carica())
    valori_esercizio.grid(row=12, column=2)
    
   # get_option_button = tk.Button(root, text="Get Option", command=option_selected)
#    get_option_button.pack(pady=5)
   # message.bind("<Button-1>", drag_start)
   # message.bind("<B1-Motion>", drag_motion)

    caricamento.mainloop()