
from Esercizio import Esercizio, Argomento, Difficolta
from Verifica import Verifica
import json

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

    n_quesiti = n_esercizi + n_problemi + n_teoria + n_definizioni
    verifica = Verifica(n_quesiti)

    filepath = f"./Smart_Test/{materia}_Esercizi.json"
    with open(filepath, "r") as file:
        dati = file.readlines()

    
    esercizi = []

    for json_str in dati:
        dati_esercizio = json.loads(json_str)

# esercizi
 #   def Sel_esercizi(numero, tipologia: str):
    for _ in range(n_esercizi):
        if dati_esercizio.get("difficoltà",{}).get("tipologia") == "esercizio":
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
                    

    for _ in range(n_problemi):
        if dati_esercizio.get("difficoltà",{}).get("tipologia") == "problema":
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

    for _ in range(n_teoria):
        if dati_esercizio.get("difficoltà",{}).get("tipologia") == "teoria":
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

    for _ in range(n_definizioni):
        if dati_esercizio.get("difficoltà",{}).get("tipologia") == "definizione":
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
 


    for esercizio in esercizi:
        verifica.aggiungi_esercizio(esercizio)

    return verifica

    
    

