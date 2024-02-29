import json
import random as rndm

from Verifica import Verifica
from Scelta_quesiti import Scegli_quesiti


def Genera(
        materia : str, 
        tematica, 
        sottotematica, 
        n_esercizi: int, 
        n_problemi:int ,
        n_definizioni:int,   
        n_teoria:int,
        n_base:int,
        n_medi:int,
        n_avanzati:int
           ):
    
    # creating counters for the difficulty of exercises
    b_count = 0
    m_count = 0
    a_count = 0

    n_livelli = [b_count, m_count, a_count]
    max_count = [n_base, n_medi, n_avanzati]

    n_quesiti = n_esercizi + n_problemi + n_teoria + n_definizioni
    verifica = Verifica(n_quesiti)

    #variabili per randomizzazione
    
    # filepath = f"./Smart_Test/{materia}_Esercizi.json"
    ## filepath for debugging
    filepath = f"./{materia}_Esercizi.json"
    try:
        with open(filepath, "r") as file:
            # dati = file.readlines()
            dati_esercizio = json.load(file)
    except FileNotFoundError:
        print(f"File '{filepath}' not found.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")

    
    # crea una lista dove salvare tutti gli indici degli esercizi già scritti
    esercizi = []
    
    esercizi, n_livelli = Scegli_quesiti(
        tipologia = "esercizio", 
        n_difficolta = n_esercizi,
        json_data = dati_esercizio,
        tema = tematica,
        sottotema = sottotematica,
        esercizi = esercizi,
        max_count = max_count, 
        n_livelli = n_livelli
        )
    
    esercizi, n_livelli = Scegli_quesiti(
        tipologia = "problema", 
        n_difficolta = n_problemi,
        json_data = dati_esercizio,
        tema = tematica,
        sottotema = sottotematica,
        esercizi = esercizi,
        max_count = max_count, 
        n_livelli = n_livelli
        )
    
    esercizi, n_livelli = Scegli_quesiti(
        tipologia = "teoria", 
        n_difficolta = n_teoria,
        json_data = dati_esercizio,
        tema = tematica,
        sottotema = sottotematica,
        esercizi = esercizi,
        max_count = max_count, 
        n_livelli = n_livelli
        )
    
    esercizi, n_livelli = Scegli_quesiti(
        tipologia = "definizione", 
        n_difficolta = n_definizioni,
        json_data = dati_esercizio,
        tema = tematica,
        sottotema = sottotematica,
        esercizi = esercizi,
        max_count = max_count, 
        n_livelli = n_livelli
        )


    for esercizio in esercizi:
        verifica.Aggiungi_esercizio(esercizio)

    return verifica

    
    

