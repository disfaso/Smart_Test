import unittest
import os
from Carica_esercizio import Creazione_dati, Append_un_file_json

class TestFileLoading(unittest.TestCase):
    def test_append_un_file_json_success(self):
        
        dato_campione = {'key': 'value'}

        # Scrivi il dato_campione su un file temporaneo
        file_path = './Test/test_file.json'
        with open(file_path, 'w') as file:
            file.write('[]')

        # Testa l'aggiunta di un dato ad un campione
        existing_data = Append_un_file_json(file_path, dato_campione)

        # Assert
        self.assertEqual(existing_data, [dato_campione])

        os.remove(file_path)

    def test_aggiungi_a_file_non_trovato(self):
        
        with self.assertRaises(FileNotFoundError):
            Append_un_file_json('./mock.json', {'key': 'value'})


if __name__ == '__main__':
    unittest.main()