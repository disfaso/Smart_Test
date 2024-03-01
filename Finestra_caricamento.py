import tkinter as tk
from Esercizio import Esercizio
from Tkinter_methods import Valori_esercizio, Chiudi_finestra
from Carica_esercizio import Creazione_dati



def Finestra_caricamento(es: Esercizio):
    """
    Apre una finestra di caricamento per aggiungere un nuovo esercizio.

    Args:
        es (Esercizio): Oggetto Esercizio a cui aggiungere i dati inseriti nella finestra.

    Returns:
        None
    """
    caricamento = tk.Tk()

    caricamento.title("Carica un esercizio")
    caricamento.geometry('1000x800')

#instruzioni per il caricamento
    message1 = tk.Label(caricamento, compound=tk.CENTER, bg="blue", text="Scrivi i parametri per l'esercizio da caricare\n")
    message1.grid(row=0, column=0)

    message = tk.Label(caricamento, compound=tk.CENTER, bg="blue", text="L'unità di apprendimento e la sottotematica indicate \nsaranno parole chiave nel generare le verifiche,\n si consiglia di prestare attenzione \nalla consistenza dei termini utilizzati")
    message.grid(row=0, column=1)

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

    

    #trasversalita
    trasversalita = tk.BooleanVar()
    trasversalita.set(False)
    cb_tras = tk.Checkbutton(caricamento, background = "light green", text="L'esercizio ha trasversalità per più materie?", variable= trasversalita)
    
    cb_tras.grid(row=5, column=0)

    #centralita
    centralita = tk.Label(caricamento, bg="light green", text="Inserire la centralita dell'esercizio alla sua sottotematica")    
    centralita.grid(row=6, column=0)

    centralita_in = tk.Entry(caricamento, validate="key")
    centralita_in.grid(row=6, column=1)
    

#Difficolta
    #dsa
    dsa = tk.BooleanVar()
    dsa.set(False)
    cb_dsa = tk.Checkbutton(caricamento, background = "light green", text="L'esercizio ha problemi per studenti con disturbi specifici dell'apprendimento?", variable= dsa)
    
    cb_dsa.grid(row=12, column=0)

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
    risposta.grid(row=11, column=0)

    risposta_in = tk.Entry(caricamento, validate="key")
    risposta_in.grid(row=11, column=1)

    def Bottone_carica():
        """
        Funzione chiamata quando il bottone di caricamento viene premuto.
        Estrae i valori dai widget e li assegna all'oggetto Esercizio, 
        quindi chiama la funzione Creazione_dati.

        Args:
            None

        Returns:
            None
        """
        Valori_esercizio(es, 
                         tematica_in, 
                         testo_in, 
                         oda_in, 
                         sottotematica_in, 
                         trasversalita, 
                         centralita_in, 
                         dsa, 
                         tip_selezionata, 
                         lvl_selezionato, 
                         selezionato, 
                         materia_in, 
                         risposta_in)
        Creazione_dati(es=es)


    def Bottone_home():
        """
        Funzione chiamata quando il bottone "Torna alla schermata home" viene premuto.
        Chiude la finestra di caricamento e apre la schermata home.

        Args:
            None

        Returns:
            None
        """
        from Finestra_home import Finestra_home
        Chiudi_finestra(caricamento)
        Finestra_home()


#bottone per fissare i valori alla variabile esercizio e chiamare il json
    valori_esercizio = tk.Button(caricamento, bg="light green", text="Carica l'esercizio", command=Bottone_carica)
    valori_esercizio.grid(row=13, column=1)
    

    home_torna = tk.Button(caricamento, bg ="yellow", text="Torna alla schermata home", command=Bottone_home)
    home_torna.grid(row=13, column=0)
   # get_option_button = tk.Button(root, text="Get Option", command=option_selected)
#    get_option_button.pack(pady=5)
   # message.bind("<Button-1>", drag_start)
   # message.bind("<B1-Motion>", drag_motion)

    caricamento.mainloop()