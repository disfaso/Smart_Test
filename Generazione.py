import json
import random as rndm

from Esercizio import Esercizio, Argomento, Difficolta
from Verifica import Verifica


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

    #variabili per randomizzazione
    
    #filepath = f"./Smart_Test/{materia}_Esercizi.json"
    ## filepath for debugging
    filepath = f"./{materia}_Esercizi.json"
    try:
        with open(filepath, "r") as file:
            # dati = file.readlines()
            dati_esercizio = json.load(file)
    except FileNotFoundError:
        print(f"File '{filepath}' not found.")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")

     #variabili per randomizzazione
    json_size = len(dati_esercizio)
    seed = rndm.randrange(json_size)
    i=0
    
    esercizi = []

 #   for json_str in dati:
 #       dati_esercizio = json.loads(json_str)

# esercizi
 #   def Sel_esercizi(numero, tipologia: str):
    # inizializzo la variabile che mi servirà per controllare di non riprendere più esercizi uguali
    j = 0

# itero fino a che non ho caricato un numero di esercizi pari a quelli richiesti
    while i < n_esercizi:
        
        j += 1

        # se ho provato tutti gli esercizi, esci dal loop 
        if j > json_size:
            #raise NameError("Non ho trovato un quesito classificato con i parametri indicati:\n tipologia : esercizio")
            print("Non ho trovato un quesito classificato con i parametri indicati:\n tipologia : esercizio")
            break

        # crea un numero randomico compreso tra zero e il totale degli esercizi nel file caricato
        seed = rndm.randrange(json_size)

        
        # crea una lista dove salvare tutti gli indici degli esercizi già scritti
        seeds = [] * json_size

        # creo un loop che prende tutti i seed fino a quello inizializzato
        for controllo in seeds[:j]:
            # se l'elemento che stiamo considerando è uguale al seed corrente, non fare nulla
            # se tutti gli elementi di seeds sono già stati chiamati, il programma non entrerà nel loop
            if controllo == seed:
                pass

            # inizializzo l'elemento nella lista da controllare dopo, genero esercizio_prova come l'esercizio in posizione seed di dati_esercizio
            else:
                seeds[j-1] = seed
                esercizio_prova = dati_esercizio[seed]

        #selezione per parole chiave date in input
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
                                    i += 1
                                                
                            if n_medi >= m_count:
                                if esercizio_prova.get("difficolta",{}).get("livello") == "medio":
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
                                    i += 1
                                
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
                                    i += 1
                    
    
    i = 0
    j = 0
    while i < n_problemi:
        j += 1
        
        if j == json_size:
            # raise NameError("Non ho trovato un quesito classificato con i parametri indicati:\n tipologia : problema")
            print("Non ho trovato un quesito classificato con i parametri indicati:\n tipologia : problema")
            break
        

        

        # crea un numero randomico compreso tra zero e il totale degli esercizi nel file caricato
        seed = rndm.randrange(json_size)

        
        # crea una lista dove salvare tutti gli indici degli esercizi già scritti
        seeds = [] * json_size

        # creo un loop che prende tutti i seed fino a quello inizializzato
        for controllo in seeds[:j]:
            # se l'elemento che stiamo considerando è uguale al seed corrente, non fare nulla
            # se tutti gli elementi di seeds sono già stati chiamati, il programma non entrerà nel loop
            if controllo == seed:
                pass

            # inizializzo l'elemento nella lista da controllare dopo, genero esercizio_prova come l'esercizio in posizione seed di dati_esercizio
            else:
                seeds[j-1] = seed
                esercizio_prova = dati_esercizio[seed]

        #selezione per parole chiave date in input
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
                                    i += 1
                                                
                            if n_medi >= m_count:
                                if esercizio_prova.get("difficolta",{}).get("livello") == "medio":
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
                                    i += 1
                                    
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
                                    i += 1

    i = 0
    j=0
    while i < n_teoria:
        j += 1
        
        if j == json_size:
            #raise NameError("Non ho trovato un quesito classificato con i parametri indicati:\n tipologia : teoria")
            print("Non ho trovato un quesito classificato con i parametri indicati:\n tipologia : teoria")
            break


        # crea un numero randomico compreso tra zero e il totale degli esercizi nel file caricato
        seed = rndm.randrange(json_size)

        
        # crea una lista dove salvare tutti gli indici degli esercizi già scritti
        seeds = [] * json_size

        # creo un loop che prende tutti i seed fino a quello inizializzato
        for controllo in seeds[:j]:
            # se l'elemento che stiamo considerando è uguale al seed corrente, non fare nulla
            # se tutti gli elementi di seeds sono già stati chiamati, il programma non entrerà nel loop
            if controllo == seed:
                pass

            # inizializzo l'elemento nella lista da controllare dopo, genero esercizio_prova come l'esercizio in posizione seed di dati_esercizio
            else:
                seeds[j-1] = seed
                esercizio_prova = dati_esercizio[seed]

        #selezione per parole chiave date in input
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
                                    i += 1
                                                
                            if n_medi >= m_count:
                                if esercizio_prova.get("difficolta",{}).get("livello") == "medio":
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
                                    i += 1
                            
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
                                    i += 1

    i = 0
    j = 0
    while i < n_definizioni:
        j += 1
        
        if j > 5*json_size:
            # raise NameError("Non ho trovato un quesito classificato con i parametri indicati:\n tipologia : definizione")
            print("Non ho trovato un quesito classificato con i parametri indicati:\n tipologia : definizione")
            break

        # crea un numero randomico compreso tra zero e il totale degli esercizi nel file caricato
        seed = rndm.randrange(json_size)

        
        # crea una lista dove salvare tutti gli indici degli esercizi già scritti
        seeds = [] * json_size

        # creo un loop che prende tutti i seed fino a quello inizializzato
        for controllo in seeds[:j]:
            # se l'elemento che stiamo considerando è uguale al seed corrente, non fare nulla
            # se tutti gli elementi di seeds sono già stati chiamati, il programma non entrerà nel loop
            if controllo == seed:
                pass

            # inizializzo l'elemento nella lista da controllare dopo, genero esercizio_prova come l'esercizio in posizione seed di dati_esercizio
            else:
                seeds[j-1] = seed
                esercizio_prova = dati_esercizio[seed]

        #selezione per parole chiave date in input
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
                                    i += 1
                                                
                            if n_medi >= m_count:
                                if esercizio_prova.get("difficolta",{}).get("livello") == "medio":
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
                                    i += 1
                            
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
                                    i += 1
 


    for esercizio in esercizi:
        verifica.Aggiungi_esercizio(esercizio)

    return verifica

    
    

