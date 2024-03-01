import tkinter as tk
from Tkinter_methods import Valida_input, Chiudi_finestra, Prima_lettera_maiuscola
from Generazione import Genera
from Scrivi import Scrivi_verifica_s



def Finestra_generazione():
    """
        Funzione che gestisce la GUI per la generazione delle verifiche

        input gestiti dalle entrate:
            teoria_in : numero di quesiti di tipologia 'teoria' richiesti
            definizioni_in : numero di quesiti di tipologia 'definizione' richiesti
            problemi_in : numero di quesiti di tipologia 'problema' richiesti
            esercizi_in : numero di  quesiti di tipologia 'esercizi' richiesti

            basilari_in : numero di esercizi di livello 'base' richiesti
            intermedi_in : numero di esercizi di livello 'medio' richiesti
            avanzati_in : numero di esercizi di livello 'avanzato' richiesti

            tematica_in: unità di apprendimento della verifica
            sottotematica_in: argomento specifico della verifica
            materia_in : materia della verifica; variabile utilizzata per l'accesso ai dati e il salvataggio
            classificazione_in : input utilizzato per distinguere verifiche diverse in fase di salvataggio
            
    """
    generazione = tk.Tk()

    generazione.title("Genera una verifica")
    generazione.geometry('1000x400')

# Create the instruction for the generation
    message = tk.Label(generazione, compound=tk.CENTER, bg="red", text="Inserisci il numero di esercizi di ogni tipologia desiderati ")
    message.grid(row=0, column=0)

    message1 = tk.Label(generazione, compound=tk.CENTER, bg="red", text="La somma degli esercizi di diverse tipologie deve essere \nuguale a quella di diverse difficoltà")
    message1.grid(row=0, column=1)

# Teoria label e input
    teoria = tk.Label(generazione, bg="orange", text="Numero quesiti di teoria")    
    teoria.grid(row=1, column=0)

    valida_input_numerico = generazione.register(Valida_input)
    teoria_in = tk.Entry(generazione, validate="key", validatecommand=(valida_input_numerico, "%P"))
    teoria_in.grid(row=1, column=1)

# Definizioni label e input
    definizioni = tk.Label(generazione, bg="orange", text="Numero di definizioni")    
    definizioni.grid(row=2, column=0)

    valida_input_numerico = generazione.register(Valida_input)
    definizioni_in = tk.Entry(generazione, validate="key", validatecommand=(valida_input_numerico, "%P"))
    definizioni_in.grid(row=2, column=1)

# Problemi label e input
    problemi = tk.Label(generazione, bg="orange", text="Numero quesiti classificati come problemi")    
    problemi.grid(row=3, column=0)

    valida_input_numerico = generazione.register(Valida_input)
    problemi_in = tk.Entry(generazione, validate="key", validatecommand=(valida_input_numerico, "%P"))
    problemi_in.grid(row=3, column=1)

# Esercizi label e input
    esercizi = tk.Label(generazione, bg="orange", text="Numero quesiti classificati come esercizi")    
    esercizi.grid(row=4, column=0)

    valida_input_numerico = generazione.register(Valida_input)
    esercizi_in = tk.Entry(generazione, validate="key", validatecommand=(valida_input_numerico, "%P"))
    esercizi_in.grid(row=4, column=1)

# Quantita di un certo livello di esercizi richiesta
    #Esercizi Base
    basilari =  tk.Label(generazione, bg="orange", text="Numero quesiti basilari richiesti nella verifica")    
    basilari.grid(row=5, column=0)

    valida_input_numerico = generazione.register(Valida_input)
    basilari_in = tk.Entry(generazione, validate="key", validatecommand=(valida_input_numerico, "%P"))
    basilari_in.grid(row=5, column=1)

    #Esercizi Medi
    intermedi = tk.Label(generazione, bg="orange", text="Numero quesiti intermedi richiesti nella verifica")
    intermedi.grid(row=6, column=0)

    valida_input_numerico = generazione.register(Valida_input)
    intermedi_in = tk.Entry(generazione, validate="key", validatecommand=(valida_input_numerico, "%P"))
    intermedi_in.grid(row=6, column=1)

    #Esercizi Avanzati
    avanzati = tk.Label(generazione, bg="orange", text="Numero quesiti avanzati richiesti nella verifica")
    avanzati.grid(row=7, column=0)

    valida_input_numerico = generazione.register(Valida_input)
    avanzati_in = tk.Entry(generazione, validate="key", validatecommand=(valida_input_numerico, "%P"))
    avanzati_in.grid(row=7, column=1)

    #materia
    materia = tk.Label(generazione, bg="orange", text="Inserire la materia a cui appartiene l'esercizio")    
    materia.grid(row=8, column=0)

    materia_in = tk.Entry(generazione, validate="key")
    materia_in.grid(row=8, column=1)

    #Tematica
    tematica = tk.Label(generazione, bg="orange", text="Inserire l'unità di apprendimento dell'esercizio")    
    tematica.grid(row=9, column=0)

    tematica_in = tk.Entry(generazione, validate="key")
    tematica_in.grid(row=9, column=1)

    #sottotematica
    sottotematica = tk.Label(generazione, bg="orange", text="Inserire la sottotematica dell'esercizio")    
    sottotematica.grid(row=10, column=0)

    sottotematica_in = tk.Entry(generazione, validate="key")
    sottotematica_in.grid(row=10, column=1)

    #classificazione verifica
    classificazione = tk.Label(generazione, bg="orange", text="Inserire una classificazione per la verifica\n (verrà inserita nel nome del documento per distinguerla da altre verifiche generate)")    
    classificazione.grid(row=11, column=0)

    classificazione_in = tk.Entry(generazione, validate="key")
    classificazione_in.grid(row=11, column=1)

    def Bottone_genera():
        """
            Assegna i valori di input a variabili istanziate, convertendo le str in int

            Chiama funzione Scrivi_verifica_s con le variabili istanziate in input

        """
        m = Prima_lettera_maiuscola(materia_in.get())
        t = tematica_in.get()
        s = sottotematica_in.get()
        c = classificazione_in.get()
        n_e = esercizi_in.get()
        n_p = problemi_in.get()
        n_t = teoria_in.get()
        n_d = definizioni_in.get()
        n_a = avanzati_in.get()
        n_m = intermedi_in.get()
        n_b = basilari_in.get()
        n_e = int(n_e)
        n_p = int(n_p)
        n_t = int(n_t)
        n_d = int(n_d)
        n_a = int(n_a)
        n_m = int(n_m)
        n_b = int(n_b)

        verifica = Genera(
            materia = m,
            tematica = t,
            sottotematica = s,
            n_esercizi = n_e,
            n_problemi = n_p,
            n_teoria = n_t,
            n_definizioni = n_d,
            n_avanzati = n_a,
            n_medi = n_m,
            n_base = n_b,
        )
        Scrivi_verifica_s(verifica=verifica, classificazione = c)

    def Bottone_home():
        from Finestra_home import Finestra_home
        Chiudi_finestra(generazione)
        Finestra_home()

    button = tk.Button(generazione,bg="orange", text="Genera la verifica", command=Bottone_genera)
    button.grid(row=12, column=1)

    home_torna = tk.Button(generazione, bg ="yellow", text="Torna alla schermata home", command=Bottone_home)
    home_torna.grid(row=12, column=0)

   # message.bind("<Button-1>", drag_start)
   # message.bind("<B1-Motion>", drag_motion)

    generazione.mainloop()
