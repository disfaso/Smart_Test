import json
import os
from Esercizio import Esercizio

def Append_a_file_json(file_path, new_data):
    existing_data = []

    # Leggi  il file se path esistente
    if os.path.exists(file_path):
        with open(file_path, "r") as json_file:
            existing_data = json.load(json_file)

    # Append il nuovo json object 
    existing_data.append(new_data)

    return existing_data

    

def Creazione_dati(es: Esercizio):
    dati = {
        "tematica" : es.tematica,
        "testo" : es.testo, 
        "materia" : es.materia,
        "risposta" : es.risposta,
	    "argomento" : {
                        "oda" : es.argomento.oda,
                        "sottotematica" : es.argomento.sottotematica,
                        "trasversalita" : es.argomento.trasversalita,
                        "centralita" : es.argomento.centralita,
                    },
        "difficolta" : {
                        "dsa" : es.difficolta.dsa,
                        "tipologia" : es.difficolta.tipologia,
                        "infamia" : es.difficolta.infamia,
                        "livello" : es.difficolta.livello,
                    }
        }
    
    organizer = str(es.materia)
    file_path = f"./Smart_Test/{organizer}_Esercizi.json"

    # controlla che il file non esista per capire se è il primo oggetto inserito
    primo_json = not os.path.exists(file_path)


# Se non è primo json inserito, ricrea l'intera lista e aggiungi i nuovi dati
    if not primo_json:
        existing_data = Append_a_file_json(file_path, dati)

# Se è il primo file, assegna alla variabile existing_data il nuovo dato da inserire        
    elif primo_json:
        existing_data = dati
        

#riscrivere il file json
    with open(file_path, "w") as json_file:    
        
        
        
        json.dump(existing_data, json_file, indent=4)

        

# scrivi json object
        
        
    
# se è la prima volta che scriviamo il file, 