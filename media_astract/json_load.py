import json
from Model import Biblioteca, Libro, Film, Oggetto_media, Pinacoteca, Quadro, Videoteca





def index(json_file):
    with open(json_file) as f:
        lettura_json = json.load(f)
    return lettura_json


def generate_object_by_key(lettura_json, lookup_key):
    searched = []
    for key, item in lettura_json.items():
        if key == lookup_key:
            found = list(item)
            for x in found:
                   if lookup_key == "Libro":
                    x = Libro(titolo=["titolo"], autore=["autore"], editore=["editore"], anno=["anno"])
                    searched.append(x)
                   elif lookup_key == "Film":
                    x = Film(titolo=["titolo"], autore=["autore"], tecnica=["tecnica"], anno=["anno"])
                    searched.append(x)
                   elif lookup_key == "Quadro":
                    x = Quadro(titolo=["titolo"], autore=["autore"], tecnica=["tecnica"], anno=["anno"])
                    searched.append(x)
    return searched


