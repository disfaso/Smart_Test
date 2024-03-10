from docx import Document
from Verifica import Verifica
import os

def Cartella_controllo(cartella_path):
    """
    Crea una cartella se non esiste già.

    Args:
        cartella_path (str): Il percorso della cartella da controllare/creare.

    Returns:
        None
    """
    if not os.path.exists(cartella_path):
        os.makedirs(cartella_path)

    else:
        pass



def Scrivi_verifica_s(verifica: Verifica, classificazione: str):
    """
    Scrive una verifica per studenti in un file .docx.

    Args:
        verifica (Verifica): Oggetto Verifica contenente gli esercizi della verifica.
        classificazione (str): La classificazione della verifica.

    Returns:
        None
    """
    tematica = verifica.esercizi[0].tematica
    sottotematica = verifica.esercizi[0].argomento.sottotematica
    materia = verifica.esercizi[0].materia
    i = 1
    file_path = f"./Smart_Test/Verifiche_{materia}/"
   

    doc = Document()

    doc.add_heading(f"Verifica di {materia}; unità: {tematica}; argomento: {sottotematica}", level=1)
    
    for esercizio in verifica.esercizi:
        titolo = f"Esercizio numero {i}"
        testo = esercizio.testo
        doc.add_heading(titolo, level=2)

        doc.add_paragraph(testo)

        i += 1

    Cartella_controllo(file_path)

    doc.save(f"{file_path}Verifica_{classificazione}.docx")