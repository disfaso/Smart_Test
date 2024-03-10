import unittest
import os
import sys
import json
import logging

# Add the parent directory of the current script to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from Carica_esercizio import Append_un_file_json
from Generazione import Leggi_json_file, Genera
from Tkinter_methods import Prima_lettera_maiuscola
from Scrivi import Cartella_controllo, Scrivi_verifica_s, Scrivi_verifica_d
from Verifica import Verifica
from Esercizio import Esercizio, Argomento, Difficolta

class TestFileLoading(unittest.TestCase):
    """
    Test per le funzioni di caricamento dei file.
    """
    def test_append_un_file_json_success(self):
        """
        Test per l'aggiunta di dati a un file JSON esistente.
        """
        
        dato_campione = {'key': 'value'}

        dato_atteso = {'key': 'value'}

        # Scrivi il dato_campione su un file temporaneo
        file_path = './test_file.json'
        with open(file_path, 'w') as file:
            file.write('[]')

        # Testa l'aggiunta di un dato ad un campione
        existing_data = Append_un_file_json(file_path, dato_campione)

        # Assert
        self.assertEqual(existing_data, [dato_atteso])

        os.remove(file_path)

    def test_aggiungi_a_file_non_trovato(self):
        """
        Test per la gestione di FileNotFoundError durante l'aggiunta di dati a un file inesistente.
        """

        logging.basicConfig(level=logging.DEBUG)

        result = None
        try:
            result = Append_un_file_json('./Test/mock.json', {'key': 'value'})
        except FileNotFoundError:
            logging.error("File not found error caught, but not expected.")

        self.assertIsNone(result, "Function should not return a result")
        
        
        logging.basicConfig(level=logging.WARNING)

    def test_aggiungi_a_file_non_json(self):
        """
        Test per la gestione di JSONDecodeError durante l'aggiunta di dati a un file non JSON.
        """
        logging.basicConfig(level=logging.DEBUG)
        with self.assertRaises(json.JSONDecodeError):
            Append_un_file_json("./Test/not.json", {'key': 'value'})

        logging.basicConfig(level=logging.WARNING)

    
    def test_lettura_file_json_conosciuto(self):
        """
        Test per la lettura dei dati da un file JSON conosciuto.
        """
        dato_campione = {'key' : 'value'}

        filepath = "./Test/test_lettura.json"

        with open(filepath, 'w') as file:
            json.dump(dato_campione, file)

        existing_data = Leggi_json_file(filepath)

        self.assertEqual(existing_data, dato_campione)

        os.remove(filepath)

    def test_leggi_un_file_non_presente(self):
        """
        Test per la gestione di FileNotFoundError durante la lettura di un file inesistente.
        """
        logging.basicConfig(level=logging.DEBUG)
        
        with self.assertRaises(FileNotFoundError):
            Leggi_json_file('./Test/mock.json')

        logging.basicConfig(level=logging.WARNING)

    def test_leggi_file_non_json(self):
        """
        Test per la gestione di JSONDecodeError durante la lettura di un file non JSON.
        """
        logging.basicConfig(level=logging.DEBUG)
        with self.assertRaises(json.JSONDecodeError):
            Leggi_json_file("./Test/not.json")
        logging.basicConfig(level=logging.WARNING)


class Formattazione_stringhe(unittest.TestCase):
    """
        Test per le funzioni di formattazione delle stringhe.
    """
    def test_Prima_lettera_maiuscola_stringa_min(self):
        """
        Test per il funzionamento di Prima_lettera_maiuscola di una stringa minuscola.
        """
        input_string = "hello world"
        expected_output = "Hello world"
        self.assertEqual(Prima_lettera_maiuscola(input_string), expected_output)

    def test_Prima_lettera_maiuscola_stringa_mai(self):
        """
        Test per il funzionamento di Prima_lettera_maiuscola di una stringa con prima lettera maiuscola.
        """
        input_string = "Hello world"
        expected_output = "Hello world"
        self.assertEqual(Prima_lettera_maiuscola(input_string), expected_output)

    def test_Prima_lettera_maiuscola_stinga_vuota(self):
        """
        Test per la gestione di una stringa vuota.
        """
        # Test input with lowercase first letter
        input_string = ""
        expected_output = ""
        self.assertEqual(Prima_lettera_maiuscola(input_string), expected_output)

    def test_Prima_lettera_maiuscola_stringa_num(self):
        """
        Test per la gestione di una stringa con primo carattere numerico
        """
        # Test input with lowercase first letter
        input_string = "123abc"
        expected_output = "123abc"
        self.assertEqual(Prima_lettera_maiuscola(input_string), expected_output)

    def test_Prima_lettera_maiuscola_stringa_tutta_mai(self):
        """
        Test per la gesstione di una stringa completamente maiuscola.
        """
        input_string = "HELLO WORLD"
        expected_output = "Hello world"
        self.assertEqual(Prima_lettera_maiuscola(input_string), expected_output)

    def test_Prima_lettera_maiuscola_stringa_generica(self):
        """
        Test per la gestione di una stringa generica.
        """
        input_string = "hElLo123WorlD"
        expected_output = "Hello123world"
        self.assertEqual(Prima_lettera_maiuscola(input_string), expected_output)


class Test_cartella_controllo(unittest.TestCase):
    """
        Test per la creazione di una cartella in caso di mancata esistenza
    """
    def test_crea_cartella_se_non_esiste(self):
        """
        Test per la creazione di una cartella se non esiste.
        """
        test_folder_path = "./test_folder"
        
        Cartella_controllo(test_folder_path)
        
        self.assertTrue(os.path.exists(test_folder_path))
        
        os.rmdir(test_folder_path)


    def test_cartella_gia_esistente(self):
        """
        Test per la gestione di una cartella già esistente.
        """
        test_folder_path = "./Test/Existing_test_folder/"
        expected_folder_path = test_folder_path
        
        os.makedirs(test_folder_path)
        
        Cartella_controllo(test_folder_path)
        
        self.assertEqual(test_folder_path, expected_folder_path)

        os.rmdir(test_folder_path)


class TestScriviVerifica(unittest.TestCase):
    """
    Classe di test per la funzione Scrivi_verifica_s.

    Metodi:
        setUp(self): Prepara gli oggetti di verifica e classificazione per i test.
        test_scrivi_verifica(self): Esegue la funzione Scrivi_verifica_s e verifica se il file .docx è stato creato correttamente.
        tearDown(self): Pulisce i file temporanei creati durante i test.
    """

    def setUp(self):
        """
        Prepara gli oggetti di verifica e classificazione per i test.
        """
        self.verifica = Verifica()
        self.verifica.esercizi = [Esercizio(
                tematica="Tematica",
                testo="Testo esercizio 1",
                argomento=Argomento(
                    oda="ODA",
                    sottotematica="Sottotematica",
                    trasversalita=True,
                    centralita=2
                ),
                difficolta=Difficolta(
                    dsa=True,
                    tipologia="problema",
                    infamia=5,
                    livello="avanzato"
                ),
                materia="Materia",
                risposta="Risposta"
            ),
            Esercizio(
                tematica="Tematica",
                testo="Testo esercizio 2",
                argomento=Argomento(
                    oda="ODA",
                    sottotematica="Sottotematica",
                    trasversalita=False,
                    centralita=2
                ),
                difficolta=Difficolta(dsa=True,
                    tipologia="problema",
                    infamia=5,
                    livello="avanzato"),
                materia="Materia",
                risposta="Risposta"
            )
        ]
        self.classificazione = "A"

    def test_scrivi_verifica_s(self):
        """
        Esegue la funzione Scrivi_verifica_s e verifica se il file .docx è stato creato correttamente.
        """
        Scrivi_verifica_s(self.verifica, self.classificazione)

        file_path = f"./Smart_Test/Verifiche_{self.verifica.esercizi[0].materia}/Verifica_{self.classificazione}.docx"
        self.assertTrue(os.path.exists(file_path), "Il file .docx per studenti non è stato creato")

    def test_scrivi_verifica_d(self):
        """
        Esegue la funzione Scrivi_verifica_d e verifica se il file .docx è stato creato correttamente.
        """
        Scrivi_verifica_d(self.verifica, self.classificazione)
        file_path_d = f"./Smart_Test/Verifiche_{self.verifica.esercizi[0].materia}/Verifica_docente_{self.classificazione}.docx"
        self.assertTrue(os.path.exists(file_path_d), "Il file .docx per docenti non è stato creato")

    def tearDown(self):
        """
        Pulisce i file temporanei creati durante i test.
        """
        file_path = f"./Smart_Test/Verifiche_{self.verifica.esercizi[0].materia}/Verifica_{self.classificazione}.docx"
        file_path_d = f"./Smart_Test/Verifiche_{self.verifica.esercizi[0].materia}/Verifica_docente_{self.classificazione}.docx"
        
        if os.path.exists(file_path):
            os.remove(file_path)

        if os.path.exists(file_path_d):
            os.remove(file_path_d)
        
        os.rmdir(f"./Smart_Test_Verifiche_{self.verifica.esercizi[0].materia}/")
        

class TestGenera(unittest.TestCase):
    """
    Testa la funzione Genera che si occupa di creare una verifica
    """

    def setUp(self):
        """
        Prepara il test creando un file JSON di esempio con dati fittizi sugli esercizi.
        """
        # Crea un dizionario con dati fittizi sugli esercizi
        path_esempio = "./Esercizi/Esempio_Esercizi.json"


        with open(path_esempio, "r") as file:
            
            self.sample_json_data = json.load(file)

        os.makedirs("./Smart_Test/Esercizi/")

        # Salva i dati fittizi JSON su un file temporaneo
        with open("./Smart_Test/Esercizi/Esempio_Esercizi.json", "w") as f:
            json.dump(self.sample_json_data, f)


    def test_genera_verifica(self):
        """
        Testa la generazione di una verifica con diversi parametri.
        """
        # Fornisci parametri di input di esempio
        materia = "Esempio"
        tematica = "tematica"
        sottotematica = "sottotematica"
        n_esercizi = 5
        n_problemi = 2
        n_definizioni = 1
        n_teoria = 2
        n_base = 3
        n_medi = 3
        n_avanzati = 4
        
        # Chiama la funzione Genera con il file JSON di dati di esempio
        verifica = Genera(materia, tematica, sottotematica, n_esercizi, n_problemi, n_definizioni, n_teoria, n_base, n_medi, n_avanzati, json_data_path="esercizi_di_prova.json")
        
        # Verifica che l'oggetto di verifica non sia None
        self.assertIsNotNone(verifica)
        
        # Verifica che l'oggetto di verifica contenga il numero corretto di esercizi
        self.assertEqual(len(verifica.esercizi), n_esercizi + n_problemi + n_definizioni + n_teoria)

    def tearDown(self):
        """
        Pulisce il test rimuovendo il file JSON di esempio.
        """
        # Pulizia: Rimuovi il file JSON di esempio
        os.remove("./Smart_Test/Esercizi/Esempio_Esercizi.json")

        os.rmdir("./Smart_Test/Esercizi")
if __name__ == '__main__':
    unittest.main()