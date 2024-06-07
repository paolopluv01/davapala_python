
# -- Modellazione classe +astratta
class Oggetto_media:

    def __init__(self, titolo, autore):
        self.titolo = titolo
        self.autore = autore

    def __repr__(self):
        return f"{self.titolo}, {self.autore}"# -- È necessaria?
    


class Media_collection:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.lista = []

    def add_media(self, Oggetto_media):
        self.lista.append(Oggetto_media)

    def stampa_lista(self):
        for l in self.lista:
            print(l)
        
    

# -- Modellazione classi derivate -- 
class Libro(Oggetto_media):
    num_progr = 0# -- variabile di classe inizializzata a 0
    def __init__(self, titolo, autore, editore, anno):
        super().__init__(titolo, autore)
        self.editore = editore # -- attributi aggiunti alle classi derivate
        self.anno = anno
        Libro.num_progr += 1# -- variabile di classe, si aggiorna a +1 ad ogni Oggetto creato

    def __repr__(self):
        return f"{self.num_progr}, {self.titolo}, {self.autore}, {self.editore}, {self.anno}"


class Quadro(Oggetto_media):
    num_progr = 0
    def __init__(self, titolo, autore, tecnica, anno):
        super().__init__(titolo, autore)
        self.tecnica = tecnica
        self. anno = anno
        Quadro.num_progr += 1

    def __repr__(self):
        return f"{self.num_progr}, {self.titolo}, {self.autore}, {self.tecnica}, {self.anno}"



class Film(Oggetto_media):
    num_progr = 0
    def __init__(self, titolo, autore, tecnica, anno):
        super().__init__(titolo, autore)
        self.tecnica = tecnica
        self. anno = anno
        Film.num_progr += 1

    def __repr__(self):
        return f"{self.num_progr}, {self.titolo}, {self.autore}, {self.tecnica}, {self.anno}"


class Biblioteca(Media_collection):
    def __init__(self, nome) -> None:
        super().__init__(nome)

        
    def add_media(self, Oggetto_media):
        if type(Oggetto_media) == Libro:
            super().add_media(Libro)
            print('Libro inserito')
        else:
            print('Inserimento sbagliato') 


class Pinacoteca(Media_collection):
    def __init__(self, nome) -> None:
        super().__init__(nome)

    def add_media(self, Oggetto_media):
        if type(Oggetto_media) == Quadro:
            super().add_media(Oggetto_media)
            print('Quadro inserito')
        else:
            print('Inserimento sbagliato')


class Videoteca(Media_collection):
    def __init__(self, nome) -> None:
        super().__init__(nome)

    def add_media(self, Oggetto_media):
        if type(Oggetto_media) == Film:
            super().add_media(Oggetto_media)
            print('Film inserito')
        else:
            print('Inserimento sbagliato')





