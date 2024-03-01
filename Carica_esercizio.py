import json
import os
import logging
from Esercizio import Esercizio

def Append_un_file_json(file_path, new_data):
    """
    Legge un file JSON esistente e aggiunge nuovi dati ad esso.

    Args:
        file_path (str): Il percorso del file JSON esistente.
        new_data (dict): I nuovi dati da aggiungere al file.

    Returns:
        list: La lista aggiornata dei dati JSON.

    """
    existing_data = []

    # Leggi  il file se path esistente
    try:
        if os.path.exists(file_path):
            with open(file_path, "r") as json_file:
                existing_data = json.load(json_file)
                 # Append il nuovo json object 
                existing_data.append(new_data)
                return existing_data
        
    except FileNotFoundError as e:
        logging.error(f"Errore nel caricare i dati JSON: {e}")
        raise e
    
    except json.JSONDecodeError as e:
        logging.error(f"Errore di decodifica dei dati JSON: {e}")
        raise e

   

    

    

def Creazione_dati(es: Esercizio):
    """
    Crea un nuovo oggetto JSON per rappresentare i dati di un esercizio 
    e lo aggiunge a un file JSON esistente o ne crea uno nuovo.

    Args:
        es (Esercizio): Esercizio da inserire nel file JSON.

    """
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

    #debugging file_path 
    #file_path = f"./{organizer}_Esercizi.json"

    # controlla che il file non esista per capire se è il primo oggetto inserito
    primo_json = not os.path.exists(file_path)


# Se non è primo json inserito, ricrea l'intera lista e aggiungi i nuovi dati
    if not primo_json:
        existing_data = Append_un_file_json(file_path, dati)

        #riscrivere il file json
        with open(file_path, "w") as json_file:    
            
            json_file.write("[\n")
            
            index = 0
            for data in existing_data:
                

                json.dump(data, json_file, indent=4)

                if index == len(existing_data) - 1:
                    json_file.write("\n")
                
                else:
                    json_file.write(",\n")
                
                index += 1

            json_file.write("]")


# Se è il primo file, assegna alla variabile existing_data il nuovo dato da inserire        
    elif primo_json:
        existing_data = dati
        
        with open(file_path, "w") as json_file:    
            
            json_file.write("[\n")
                

            json.dump(existing_data, json_file, indent=4)


            json_file.write("\n]")


        

