from abc import ABC, abstractmethod

class OggettoMedia(ABC):
    """Base abstract class for media objects."""
    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore

    def __repr__(self):
        return f"{self.titolo}, {self.autore}"

class Libro(OggettoMedia):
    num_progr = 0
    def __init__(self, titolo, autore, editore, anno):
        super().__init__(titolo, autore)
        self.editore = editore
        self.anno = anno
        Libro.num_progr += 1
        self.id = Libro.num_progr

    def __repr__(self):
        return f"{self.id}, {self.titolo}, {self.autore}, {self.editore}, {self.anno}"

class Quadro(OggettoMedia):
    num_progr = 0
    def __init__(self, titolo, autore, tecnica, anno):
        super().__init__(titolo, autore)
        self.tecnica = tecnica
        self.anno = anno
        Quadro.num_progr += 1
        self.id = Quadro.num_progr

    def __repr__(self):
        return f"{self.id}, {self.titolo}, {self.autore}, {self.tecnica}, {self.anno}"

class Film(OggettoMedia):
    num_progr = 0
    def __init__(self, titolo, autore, tecnica, anno):
        super().__init__(titolo, autore)
        self.tecnica = tecnica
        self.anno = anno
        Film.num_progr += 1
        self.id = Film.num_progr

    def __repr__(self):
        return f"{self.id}, {self.titolo}, {self.autore}, {self.tecnica}, {self.anno}"

class MediaCollection:
    def __init__(self, nome):
        self.nome = nome
        self.lista = []

    def add_media(self, obj):
        if not isinstance(obj, OggettoMedia):
            print("Elemento non valido")
            return
        self.lista.append(obj)
        print(f"{obj.__class__.__name__} inserito")

    def stampa_lista(self):
        for l in self.lista:
            print(l)

class Biblioteca(MediaCollection):
    def add_media(self, obj):
        if isinstance(obj, Libro):
            super().add_media(obj)
        else:
            print("Inserimento sbagliato: non è un Libro")

class Pinacoteca(MediaCollection):
    def add_media(self, obj):
        if isinstance(obj, Quadro):
            super().add_media(obj)
        else:
            print("Inserimento sbagliato: non è un Quadro")

class Videoteca(MediaCollection):
    def add_media(self, obj):
        if isinstance(obj, Film):
            super().add_media(obj)
        else:
            print("Inserimento sbagliato: non è un Film")