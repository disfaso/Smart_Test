import tkinter as tk
from Tkinter_methods import Valida_input



def Finestra_generazione():
    generazione = tk.Tk()

    generazione.title("Genera una verifica")
    generazione.geometry('1000x800')

# Create the instruction for the generation
    message = tk.Label(generazione, compound=tk.CENTER, bg="yellow", text="Trascina qui l'quesito")
    message.grid(row=0, column=4)

# Teoria label e input
    teoria = tk.Label(generazione, bg="light blue", text="Numero quesiti di teoria")    
    teoria.grid(row=1, column=0)

    valida_input_numerico = generazione.register(Valida_input)
    teoria_in = tk.Entry(generazione, validate="key", validatecommand=(valida_input_numerico, "%P"))
    teoria_in.grid(row=1, column=1)

# Definizioni label e input
    definizioni = tk.Label(generazione, bg="light blue", text="Numero di definizioni")    
    definizioni.grid(row=2, column=0)

    valida_input_numerico = generazione.register(Valida_input)
    definizioni_in = tk.Entry(generazione, validate="key", validatecommand=(valida_input_numerico, "%P"))
    definizioni_in.grid(row=2, column=1)

# Problemi label e input
    problemi = tk.Label(generazione, bg="light blue", text="Numero quesiti classificati come problemi")    
    problemi.grid(row=3, column=0)

    valida_input_numerico = generazione.register(Valida_input)
    problemi_in = tk.Entry(generazione, validate="key", validatecommand=(valida_input_numerico, "%P"))
    problemi_in.grid(row=3, column=1)

# Esercizi label e input
    esercizi = tk.Label(generazione, bg="light blue", text="Numero quesiti classificati come esercizi")    
    esercizi.grid(row=4, column=0)

    valida_input_numerico = generazione.register(Valida_input)
    esercizi_in = tk.Entry(generazione, validate="key", validatecommand=(valida_input_numerico, "%P"))
    esercizi_in.grid(row=4, column=1)

# Quantità di un certo livello di esercizi richiesta
    #Esercizi Base
    basilari =  tk.Label(generazione, bg="light blue", text="Numero quesiti basilari richiesti nella verifica")    
    basilari.grid(row=6, column=0)

    valida_input_numerico = generazione.register(Valida_input)
    basilari_in = tk.Entry(generazione, validate="key", validatecommand=(valida_input_numerico, "%P"))
    basilari_in.grid(row=6, column=1)

    #Esercizi Medi
    intermedi = tk.Label(generazione, bg="light blue", text="Numero quesiti intermedi richiesti nella verifica")
    intermedi.grid(row=7, column=0)

    valida_input_numerico = generazione.register(Valida_input)
    intermedi_in = tk.Entry(generazione, validate="key", validatecommand=(valida_input_numerico, "%P"))
    intermedi_in.grid(row=6, column=1)

    #Esercizi Avanzati
    avanzati = tk.Label(generazione, bg="light blue", text="Numero quesiti avanzati richiesti nella verifica")
    avanzati.grid(row=7, column=0)

    valida_input_numerico = generazione.register(Valida_input)
    avanzati_in = tk.Entry(generazione, validate="key", validatecommand=(valida_input_numerico, "%P"))
    avanzati_in.grid(row=7, column=1)


    button = tk.Button(generazione, text="Cliccami", command="<Button-1>")
    button.grid(row=20, column=12)

   # message.bind("<Button-1>", drag_start)
   # message.bind("<B1-Motion>", drag_motion)

    generazione.mainloop()
