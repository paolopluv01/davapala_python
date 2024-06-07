'''
Dal file main.py si deve poter 
- caricare il file json,
- chiamare una funzione che crea gli oggetti Libro, Film e Quadro in 3 liste separate per Libro, Fil e Quadro,
- creare gli oggetti Biblioteca, Videoteca e Pinacoteca
- aggiungere gli oggetti nel catalogo corrispondente,
- stampare a terminale il catalogo corrispondente alla Media_collections
- riportare i record in un databese(Mysql, Mongo, o Firebase)
'''
import os
from os.path import join, dirname
from dotenv import load_dotenv
from json_load import index, generate_object_by_key
from Model import Libro, Biblioteca, Videoteca, Pinacoteca

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

FILENAME = os.environ.get("FILENAME")

def main():

    lookup_key = input("Ricerca per key: ")

    b1 = Biblioteca("Kaspar")
    v1 = Videoteca("Columbia")
    p1 = Pinacoteca("Prado")
    json = index(FILENAME)

    search = generate_object_by_key(json, lookup_key)
    for obj in search:
        b1.add_media(obj)
    b1.stampa_lista()
   
    for obj in search:
        p1.add_media(obj)
    p1.stampa_lista()
   

if __name__ == "__main__":
    main()