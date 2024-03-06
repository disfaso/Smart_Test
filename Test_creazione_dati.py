import unittest
import os
import json
import logging
from Carica_esercizio import Append_un_file_json
from Generazione import Leggi_json_file
from Tkinter_methods import Prima_lettera_maiuscola
from Scrivi import Cartella_controllo

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
        file_path = './Test/test_file.json'
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
        test_folder_path = "./Test/test_folder"
        
        Cartella_controllo(test_folder_path)
        
        self.assertTrue(os.path.exists(test_folder_path))
        
        os.rmdir(test_folder_path)


    def test_cartella_gia_esistente(self):
        """
        Test per la gestione di una cartella già esistente.
        """
        test_folder_path = "./Test/Existing_test_tolder"
        
        os.makedirs(test_folder_path)
        
        Cartella_controllo(test_folder_path)
        
        self.assertTrue(os.path.exists(test_folder_path))


    



if __name__ == '__main__':
    unittest.main()