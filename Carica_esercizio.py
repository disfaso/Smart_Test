import json
from Esercizio import Esercizio

def Creazione_dati(es: Esercizio):
    dati = {
        "tematica" : es.tematica,
        "testo" : es.testo, 
        "materia" : es.materia,
        "risposta" : es.risposta,
	    "argomento" : {
                        "oda" : es.argomento.oda,
                        "sottotematica" : es.argomento.sottotematica,
                        "trasversalità" : es.argomento.trasversalità,
                        "centralità" : es.argomento.centralità,
                    },
        "difficoltà" : {
                        "DSA" : es.difficoltà.dsa,
                        "tipologia" : es.difficoltà.tipologia,
                        "infamia" : es.difficoltà.infamia,
                        "livello" : es.difficoltà.livello,
                    }
        }
    
    organizer = str(es.materia)
    file_path = f"./Smart_Test/{organizer}_Esercizi.json"
    json.dump(dati, open(file_path, "w"), indent=4)