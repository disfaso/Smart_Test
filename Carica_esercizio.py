import json
from Esercizio import Esercizio

def Creazione_dati(es: Esercizio):
    dati = {
  "tematica" : es.tematica,
  "testo" : es.testo, 
	"argomento" : {
    "obiettivi di apprendimento" : " ",
    "sottotematica" : "moto rettilineo uniforme",
    "trasversalità" : " ",
    "centralità" : "3",
  },
  "difficoltà" : {
    "DSA" : "2",
    "tipologia" : "problema",
    "tnfamia" : "5"
    "livello" : "medio",
  }
  "materia" : es.materia,
  "risposta" : es.risposta,
}