
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
    ## filepath for debugging
    # filepath = f"./{materia}_Esercizi.json"
    try:
        with open(filepath, "r") as file:
            # dati = file.readlines()
            dati_esercizio = json.load(file)
    except FileNotFoundError:
        print(f"File '{filepath}' not found.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
    
    esercizi = []

 #   for json_str in dati:
 #       dati_esercizio = json.loads(json_str)

# esercizi
 #   def Sel_esercizi(numero, tipologia: str):
    #n_esercizi deve essere randomizzato in qualche modo
    for esercizio_prova in dati_esercizio[:5]:
            if esercizio_prova.get("difficolta",{}).get("tipologia") == "esercizio":
                if esercizio_prova.get("tematica") == tematica:
                    if esercizio_prova.get("argomento", {}).get("sottotematica") == sottotematica:
                        if n_avanzati >= a_count:
                            if esercizio_prova.get("difficolta",{}).get("livello") == "avanzati":
                                esercizio = Esercizio(
                                                tematica=esercizio_prova.get("tematica", ""),
                                                testo=esercizio_prova.get("testo", ""),
                                                argomento=Argomento(**esercizio_prova.get("argomento", {})),
                                                difficolta=Difficolta(**esercizio_prova.get("difficolta", {})),
                                                materia=esercizio_prova.get("materia", ""),
                                                risposta=esercizio_prova.get("risposta", "")
                                            )
                                esercizi.append(esercizio)
                                a_count += 1
                                        
                        if n_medi >= m_count:
                            if esercizio_prova.get("difficolta",{}).get("livello") == "medi":
                                esercizio = Esercizio(
                                                tematica=esercizio_prova.get("tematica", ""),
                                                testo=esercizio_prova.get("testo", ""),
                                                argomento=Argomento(**esercizio_prova.get("argomento", {})),
                                                difficolta=Difficolta(**esercizio_prova.get("difficolta", {})),
                                                materia=esercizio_prova.get("materia", ""),
                                                risposta=esercizio_prova.get("risposta", "")
                                            )
                                esercizi.append(esercizio)
                                m_count += 1
                        
                        if n_base >= b_count:
                            if esercizio_prova.get("difficolta",{}).get("livello") == "base":
                                esercizio = Esercizio(
                                                tematica=esercizio_prova.get("tematica", ""),
                                                testo=esercizio_prova.get("testo", ""),
                                                argomento=Argomento(**esercizio_prova.get("argomento", {})),
                                                difficolta=Difficolta(**esercizio_prova.get("difficolta", {})),
                                                materia=esercizio_prova.get("materia", ""),
                                                risposta=esercizio_prova.get("risposta", "")
                                            )
                                esercizi.append(esercizio)
                                b_count += 1    
                    

    for esercizio_prova in dati_esercizio[:n_problemi]:
        if esercizio_prova.get("difficolta",{}).get("tipologia") == "problema":
            if esercizio_prova.get("tematica") == tematica:
                if esercizio_prova.get("argomento", {}).get("sottotematica") == sottotematica:
                    if n_avanzati >= a_count:
                        if esercizio_prova.get("difficolta",{}).get("livello") == "avanzati":
                            esercizio = Esercizio(
                                            tematica=esercizio_prova.get("tematica", ""),
                                            testo=esercizio_prova.get("testo", ""),
                                            argomento=Argomento(**esercizio_prova.get("argomento", {})),
                                            difficolta=Difficolta(**esercizio_prova.get("difficolta", {})),
                                            materia=esercizio_prova.get("materia", ""),
                                            risposta=esercizio_prova.get("risposta", "")
                                        )
                            esercizi.append(esercizio)
                            a_count += 1
                                        
                    elif n_medi >= m_count:
                        if esercizio_prova.get("difficolta",{}).get("livello") == "medi":
                            esercizio = Esercizio(
                                            tematica=esercizio_prova.get("tematica", ""),
                                            testo=esercizio_prova.get("testo", ""),
                                            argomento=Argomento(**esercizio_prova.get("argomento", {})),
                                            difficolta=Difficolta(**esercizio_prova.get("difficolta", {})),
                                            materia=esercizio_prova.get("materia", ""),
                                            risposta=esercizio_prova.get("risposta", "")
                                        )
                            esercizi.append(esercizio)
                            m_count += 1
                            
                    elif n_base >= b_count:
                        if esercizio_prova.get("difficolta",{}).get("livello") == "base":
                            esercizio = Esercizio(
                                            tematica=esercizio_prova.get("tematica", ""),
                                            testo=esercizio_prova.get("testo", ""),
                                            argomento=Argomento(**esercizio_prova.get("argomento", {})),
                                            difficolta=Difficolta(**esercizio_prova.get("difficolta", {})),
                                            materia=esercizio_prova.get("materia", ""),
                                            risposta=esercizio_prova.get("risposta", "")
                                        )
                            esercizi.append(esercizio)
                            b_count += 1  

    for esercizio_prova in dati_esercizio[:n_teoria]:
            if esercizio_prova.get("difficolta",{}).get("tipologia") == "teoria":
                if esercizio_prova.get("tematica") == tematica:
                    if esercizio_prova.get("argomento", {}).get("sottotematica") == sottotematica:
                        if n_avanzati >= a_count:
                            if esercizio_prova.get("difficolta",{}).get("livello") == "avanzati":
                                esercizio = Esercizio(
                                                tematica=esercizio_prova.get("tematica", ""),
                                                testo=esercizio_prova.get("testo", ""),
                                                argomento=Argomento(**esercizio_prova.get("argomento", {})),
                                                difficolta=Difficolta(**esercizio_prova.get("difficolta", {})),
                                                materia=esercizio_prova.get("materia", ""),
                                                risposta=esercizio_prova.get("risposta", "")
                                            )
                                esercizi.append(esercizio)
                                a_count += 1
                                            
                        elif n_medi >= m_count:
                            if esercizio_prova.get("difficolta",{}).get("livello") == "medi":
                                esercizio = Esercizio(
                                                tematica=esercizio_prova.get("tematica", ""),
                                                testo=esercizio_prova.get("testo", ""),
                                                argomento=Argomento(**esercizio_prova.get("argomento", {})),
                                                difficolta=Difficolta(**esercizio_prova.get("difficolta", {})),
                                                materia=esercizio_prova.get("materia", ""),
                                                risposta=esercizio_prova.get("risposta", "")
                                            )
                                esercizi.append(esercizio)
                                m_count += 1
                        
                        elif n_base >= b_count:
                            if esercizio_prova.get("difficolta",{}).get("livello") == "base":
                                esercizio = Esercizio(
                                                tematica=esercizio_prova.get("tematica", ""),
                                                testo=esercizio_prova.get("testo", ""),
                                                argomento=Argomento(**esercizio_prova.get("argomento", {})),
                                                difficolta=Difficolta(**esercizio_prova.get("difficolta", {})),
                                                materia=esercizio_prova.get("materia", ""),
                                                risposta=esercizio_prova.get("risposta", "")
                                            )
                                esercizi.append(esercizio)
                                b_count += 1  

    for esercizio_prova in dati_esercizio[:n_definizioni]:
            if esercizio_prova.get("difficolta",{}).get("tipologia") == "definizione":
                if esercizio_prova.get("tematica") == tematica:
                    if esercizio_prova.get("argomento", {}).get("sottotematica") == sottotematica:
                        if n_avanzati >= a_count:
                            if esercizio_prova.get("difficolta",{}).get("livello") == "avanzati":
                                esercizio = Esercizio(
                                                tematica=esercizio_prova.get("tematica", ""),
                                                testo=esercizio_prova.get("testo", ""),
                                                argomento=Argomento(**esercizio_prova.get("argomento", {})),
                                                difficolta=Difficolta(**esercizio_prova.get("difficolta", {})),
                                                materia=esercizio_prova.get("materia", ""),
                                                risposta=esercizio_prova.get("risposta", "")
                                            )
                                esercizi.append(esercizio)
                                a_count += 1
                                            
                        elif n_medi >= m_count:
                            if esercizio_prova.get("difficolta",{}).get("livello") == "medi":
                                esercizio = Esercizio(
                                                tematica=esercizio_prova.get("tematica", ""),
                                                testo=esercizio_prova.get("testo", ""),
                                                argomento=Argomento(**esercizio_prova.get("argomento", {})),
                                                difficolta=Difficolta(**esercizio_prova.get("difficolta", {})),
                                                materia=esercizio_prova.get("materia", ""),
                                                risposta=esercizio_prova.get("risposta", "")
                                            )
                                esercizi.append(esercizio)
                                m_count += 1
                        
                        elif n_base >= b_count:
                            if esercizio_prova.get("difficolta",{}).get("livello") == "base":
                                esercizio = Esercizio(
                                                tematica=esercizio_prova.get("tematica", ""),
                                                testo=esercizio_prova.get("testo", ""),
                                                argomento=Argomento(**esercizio_prova.get("argomento", {})),
                                                difficolta=Difficolta(**esercizio_prova.get("difficolta", {})),
                                                materia=esercizio_prova.get("materia", ""),
                                                risposta=esercizio_prova.get("risposta", "")
                                            )
                                esercizi.append(esercizio)
                                b_count += 1 
 


    for esercizio in esercizi:
        verifica.Aggiungi_esercizio(esercizio)

    return verifica

    
    

