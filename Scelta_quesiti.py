import random as rndm
from Esercizio import Esercizio, Argomento, Difficolta

def Controlla_semi(seeds, j:int):
    for controllo in seeds[:j+1]:
        if controllo == seeds:
            return False
            
    
    return True


def Scegli_quesiti(tipologia, n_quesiti, n_difficolta, json_data, tema, sottotema, esercizi):
    global max_count
    
    i = 0
    j = 0
    seeds = [0] * len(json_data)

    while i < n_quesiti:
        
        if j == len(json_data):
            print(f"Non ho trovato un quesito classificato con i parametri indicati:\n tema: {tema}, sottotema: {sottotema}")
            break

        seed = rndm.randrange(len(json_data))

        if Controlla_semi(seeds=seeds, j=j):
                seeds[j - 1] = seed
                esercizio_prova = json_data[seed]

                if (esercizio_prova.get("tematica") == tema and
                        esercizio_prova.get("argomento", {}).get("sottotematica") == sottotema):
                    if n_difficolta >= max_count:
                        if esercizio_prova.get("difficolta", {}).get("livello") == max_count:
                            esercizio = Esercizio(
                                tematica=esercizio_prova.get("tematica", ""),
                                testo=esercizio_prova.get("testo", ""),
                                argomento=Argomento(**esercizio_prova.get("argomento", {})),
                                difficolta=Difficolta(**esercizio_prova.get("difficolta", {})),
                                materia=esercizio_prova.get("materia", ""),
                                risposta=esercizio_prova.get("risposta", "")
                            )
                            esercizi.append(esercizio)
                            max_count += 1
                            i += 1
                
                j += 1