import random


# -- Modellazione classe +astratta
class Oggetto_media:
    def __init__(self, id, titolo, autore):
        self.id = id
        self.titolo = titolo
        self.autore = autore

    def _val(self):
        val = id(self)
        return val



class Media_collection:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.lista = []

    def add_media(self, Oggetto_media):
        self.lista.append(Oggetto_media)
        
    

# -- Modellazione classi derivate -- 
class Libro(Oggetto_media):
    def __init__(self, id, titolo, autore, editore, anno):
        super().__init__(id, titolo, autore)
        self.editore = editore # -- attributi aggiunti alle classi derivate
        self.anno = anno
        


class Quadro(Oggetto_media):
    def __init__(self, id, titolo, autore, tecnica, anno):
        super().__init__(id, titolo, autore)
        self.tecnica = tecnica
        self. anno = anno



class Film(Oggetto_media):
    def __init__(self, id, titolo, autore, tecnica, anno):
        super().__init__(id, titolo, autore)
        self.tecnica = tecnica
        self. anno = anno


class Biblioteca(Media_collection):
    def __init__(self, nome) -> None:
        super().__init__(nome)

    def add_media(self, Oggetto_media):# -- considerare di inserire il decoratore @
        if type(Oggetto_media) != Libro:
            print('Non è un libro!')
        else:
            return super().add_media(Oggetto_media)


class Pinacoteca(Media_collection):
    def __init__(self, nome) -> None:
        super().__init__(nome)


class Videoteca(Media_collection):
    def __init__(self, nome) -> None:
        super().__init__(nome)





# -- Esecuzione script --
q1 = Libro(1,'Pinocchio', 'Collodi', 'Utet', '1976')
f1 = Film(1,'Topolino', 'Walt Disney', 'animazione', '1934')
d1 = Quadro(3, 'Picasso', 'Ritratto', 'tempera', '1923')

biblio1 = Biblioteca('Comunale')
biblio1.add_media(q1)

pina1 = Pinacoteca('Moderna')
pina1.add_media(d1)
print(Libro._val(q1))#-- mostra il valore unico della funzione id che identifica l'oggetto libro q1
