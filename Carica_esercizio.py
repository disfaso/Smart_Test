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

    with open(file_path, "a") as json_file:
        json.dump(dati, json_file, indent=4)
        json_file.write("\n")
    # json.dump(dati, open(file_path, "w"), indent=4)