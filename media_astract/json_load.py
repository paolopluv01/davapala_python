import json
from Model import Libro, Film, Quadro


filename = '/Users/paolopluviano/Documents/GitHub/davapala_python/media_astract/source/dati.json'


def index(json_file):
    with open(json_file) as f:
        d = json.load(f)
    return d


lettura_json = index(filename)

for key, item in lettura_json.items():
    if key == "Libro":
        libri = list(item)# --lista di items di tipo Libro
        for m in libri:# --libri; lista temporanea dove conservare i values.
            m = Libro(titolo=["titolo"], autore=["autore"], editore=["editore"], anno=["anno"])# --crea oggetti Libro--
    elif key == "Film":
        movies = list(item)
        for m in movies:
            m = Film(titolo=["titolo"], autore=["autore"], tecnica=["tecnica"], anno=["anno"])
    else :
        quadri = list(item)
        for m in quadri:
            m = Quadro(titolo=["titolo"], autore=["autore"], tecnica=["tecnica"], anno=["anno"])



