from docx import Document
from Verifica import Verifica
import os

def cartella_controllo(cartella_path):
    if not os.path.exists(cartella_path):
        os.makedirs(cartella_path)



def Scrivi_verifica_s(verifica: Verifica):
    """
        Scrive verifica per studenti in un .docx
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

    cartella_controllo(file_path)

    doc.save(f"{file_path}Verifica.docx")