import random as rndm
from Esercizio import Esercizio, Argomento, Difficolta

def Controlla_semi(seeds, j:int):
    """
        Controlla se un numero generato casualmente è già stato utilizzato.

        Args:
            seeds (list): Lista contenente i numeri generati casualmente.
            j (int): Indice del numero corrente generato casualmente.

        Returns:
            bool: True se il numero generato casualmente non è stato utilizzato, altrimenti False.

    """
    for controllo in seeds[:j+1]:
        if controllo == seeds:
            return False
            
    
    return True


def Scegli_quesiti(tipologia, n_difficolta, json_data, tema, sottotema, esercizi, max_count, n_livelli):
    """
            Seleziona e aggiunge quesiti alla lista degli esercizi in base ai parametri specificati.

    Args:
        tipologia (str): La tipologia di quesito da selezionare.
        n_difficolta (int): Il numero totale di quesiti da selezionare.
        json_data (list): Lista contenente i dati dei quesiti in formato JSON.
        tema (str): Il tema principale dei quesiti da selezionare.
        sottotema (str): Il sottotema dei quesiti da selezionare.
        esercizi (list): Lista degli esercizi a cui aggiungere i quesiti selezionati.
        max_count (list): Lista contenente il numero massimo di quesiti per ogni livello di difficoltà.
        n_livelli (list): Lista contenente il numero di quesiti selezionati per ogni livello di difficoltà.

    Returns:
        tuple: Una tupla contenente la lista aggiornata degli esercizi con i quesiti selezionati e il numero di quesiti selezionati per ogni livello di difficoltà.
    """
    
    i = 0
    j = 0
    seeds = [0] * len(json_data)
    esercizi_selezionati = esercizi

    while i < n_difficolta:
        
        if j == len(json_data):
            print(f"Non ho trovato un quesito classificato con i parametri indicati:\n tema: {tema}, sottotema: {sottotema}")
            break

        seed = rndm.randrange(len(json_data))

        if Controlla_semi(seeds=seeds, j=j):
            seeds[j - 1] = seed
            esercizio_prova = json_data[seed]
            
            if esercizio_prova.get("difficolta", {}).get("tipologia") == tipologia:
                if (esercizio_prova.get("tematica") == tema and
                        esercizio_prova.get("argomento", {}).get("sottotematica") == sottotema):
                    for index, n in n_livelli:
                        livelli=["base", "medio", "avanzato"]
                        if n < max_count[index]:
                            if esercizio_prova.get("difficolta", {}).get("livello") == livelli[index]:
                                esercizio = Esercizio(
                                    tematica=esercizio_prova.get("tematica", ""),
                                    testo=esercizio_prova.get("testo", ""),
                                    argomento=Argomento(**esercizio_prova.get("argomento", {})),
                                    difficolta=Difficolta(**esercizio_prova.get("difficolta", {})),
                                    materia=esercizio_prova.get("materia", ""),
                                    risposta=esercizio_prova.get("risposta", "")
                                )
                                esercizi_selezionati.append(esercizio)
                                n_livelli[index] += 1
                                i += 1
                
                j += 1

    return esercizi_selezionati, n_livelli