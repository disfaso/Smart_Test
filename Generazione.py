import tkinter as tk
from Finestra_generazione import Finestra_generazione
from Esercizio import Esercizio, Argomento, Difficolta

def Genera(
        materia : str, 
        tematica, 
        sottotematica, 
        n_esercizi, 
        n_problemi,
        n_definizioni,   
        n_teoria,
        n_base,
        n_medi,
        n_avanzati
           ):
    
    # creating counters for the difficulty of exercises
    b_count = 0
    m_count = 0
    a_count = 0


    filepath = f"./Smart_Test/{materia}_Esercizi.json"
    with open(filepath, "r") as file:
        dati = file.readlines()

    
    esercizi = []

    for json_str in dati:
        dati_esercizio = json.load(json_str)

# esercizi
    def Sel_esercizi(numero, tipologia: str):
            for _ in range(numero):
                if dati_esercizio.get("difficoltà",{}).get("tipologia") == tipologia:
                    if dati_esercizio.get("tematica") == tematica:
                        if dati_esercizio.get("argomento", {}).get("sottotematica") == sottotematica:
                            if n_avanzati >= a_count:
                                if dati_esercizio.get("difficoltà",{}).get("livello") == "avanzati":
                                    esercizio = Esercizio(
                                                    tematica=dati_esercizio.get("tematica", ""),
                                                    testo=dati_esercizio.get("testo", ""),
                                                    argomento=Argomento(**dati_esercizio.get("argomento", {})),
                                                    difficolta=Difficolta(**dati_esercizio.get("difficolta", {})),
                                                    materia=dati_esercizio.get("materia", ""),
                                                    risposta=dati_esercizio.get("risposta", "")
                                                )
                                    esercizi.append(esercizio)
                                    a_count += 1
                                    
                            elif n_medi >= m_count:
                                if dati_esercizio.get("difficoltà",{}).get("livello") == "medi":
                                    esercizio = Esercizio(
                                                    tematica=dati_esercizio.get("tematica", ""),
                                                    testo=dati_esercizio.get("testo", ""),
                                                    argomento=Argomento(**dati_esercizio.get("argomento", {})),
                                                    difficolta=Difficolta(**dati_esercizio.get("difficolta", {})),
                                                    materia=dati_esercizio.get("materia", ""),
                                                    risposta=dati_esercizio.get("risposta", "")
                                                )
                                    esercizi.append(esercizio)
                                    m_count += 1
                    
                            elif n_base >= b_count:
                                if dati_esercizio.get("difficoltà",{}).get("livello") == "base":
                                    esercizio = Esercizio(
                                                    tematica=dati_esercizio.get("tematica", ""),
                                                    testo=dati_esercizio.get("testo", ""),
                                                    argomento=Argomento(**dati_esercizio.get("argomento", {})),
                                                    difficolta=Difficolta(**dati_esercizio.get("difficolta", {})),
                                                    materia=dati_esercizio.get("materia", ""),
                                                    risposta=dati_esercizio.get("risposta", "")
                                                )
                                    esercizi.append(esercizio)
                                    b_count += 1    
                    
    Sel_esercizi(n_esercizi, "esercizi")
    Sel_esercizi(n_problemi, "problemi")
    Sel_esercizi(n_teoria, "teoria")  
    Sel_esercizi(n_definizioni, "definizioni")          



    
    

