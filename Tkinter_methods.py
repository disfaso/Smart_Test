from tkinter import messagebox
from Esercizio import Esercizio

def drag_start(event):
    """
    Inizia il trascinamento dell'oggetto quando viene premuto il pulsante del mouse.

    Args:
        event: L'evento del mouse che ha attivato la funzione.

    Returns:
        None
    """
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    """
    Gestisce il movimento dell'oggetto durante il trascinamento del mouse.

    Args:
        event: L'evento del mouse che ha attivato la funzione.

    Returns:
        None
    """
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)

def Valida_input(testo):
    """
    Verifica se l'input è valido.

    Args:
        testo (str): Il testo da validare.

    Returns:
        bool: True se l'input è valido, altrimenti False.
    """
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
    """
    Aggiorna i valori di un oggetto Esercizio con i valori forniti.

    Args:
        ex (Esercizio): L'oggetto Esercizio da aggiornare.
        tematica (str): La tematica dell'esercizio.
        testo (str): Il testo dell'esercizio.
        oda (str): Gli obiettivi di apprendimento dell'esercizio.
        sottotematica (str): La sottotematica dell'esercizio.
        trasversalita (bool): Indica se l'esercizio ha trasversalità per più materie.
        centralita (int): La centralità dell'esercizio alla sua sottotematica.
        dsa (bool): Indica se l'esercizio è adatto per studenti con disturbi specifici dell'apprendimento.
        tipologia (str): La tipologia dell'esercizio.
        infamia (int): Il livello di infamia dell'esercizio.
        livello (str): Il livello di difficoltà dell'esercizio.
        materia (str): La materia a cui appartiene l'esercizio.
        risposta (str): La risposta corretta dell'esercizio.

    Returns:
        None
    """
    ex.materia = Prima_lettera_maiuscola(materia.get())
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

def Chiudi_finestra(root):
        root.destroy()


def Prima_lettera_maiuscola(s):
    """
    Rende maiuscola la prima lettera di una stringa se non è già in maiuscolo e converti le altre lettere in minuscolo.

    Args:
        s (str): La stringa di input.

    Returns:
        str: La stringa modificata con la prima lettera in maiuscolo e le altre lettere in minuscolo, 
        oppure la stringa originale se la prima lettera è già in maiuscolo o la stringa è vuota.
    """
    if s:
        
        s = s[0].upper() + s[1:].lower()
    return s

def Controlla_slash(s):
    """
    Sostituisce tutti i caratteri '/' nella stringa con il carattere '_'.

    Args:
        s (str): La stringa di input da controllare.

    Returns:
        str: La stringa modificata con tutti i caratteri '/' sostituiti con il carattere '_'.
    """
    return s.replace('/', '_')


def Controlla_somme(
        n_e,
        n_p,
        n_t,
        n_d,
        n_b,
        n_m,
        n_a
):
    """
    Controlla che la somma dei quesiti di diverse tipologie sia uguale alla somma dei quesiti di diversi livelli.

    Args:
        n_e (int): Numero di quesiti di tipo esercizio.
        n_p (int): Numero di quesiti di tipo problema.
        n_t (int): Numero di quesiti di tipo teoria.
        n_d (int): Numero di quesiti di tipo definizione.
        n_b (int): Numero di quesiti di livello base.
        n_m (int): Numero di quesiti di livello medio.
        n_a (int): Numero di quesiti di livello avanzato.

    Returns:
        bool: True se le somme dei quesiti di tipologia e livello non corrispondono, False altrimenti.
    """    
    sum_tipologia = n_e + n_p + n_t + n_d
    sum_livello = n_a + n_m + n_b

    if sum_tipologia != sum_livello:
        
        messagebox.showerror("Errore", "La somma dei quesiti di diverse tipologie deve essere uguale alla somma dei quesiti di diverso livello.")
        return True
    
    else:
        return False