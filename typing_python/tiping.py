import csv
from typing import List

# --- Class modeling ---

class Libro:
    """
    Rappresenta un libro con un titolo e un autore.
    """
    def __init__(self, titolo: str, autore: str):
        self.titolo: str = titolo
        self.autore: str = autore

    def __repr__(self) -> str:
        return f"Libro(titolo='{self.titolo}', autore='{self.autore}')"

    def __str__(self) -> str:
        return f"{self.titolo}, {self.autore}"

class Biblioteca:
    """
    Rappresenta una biblioteca che contiene un catalogo di libri.
    """
    def __init__(self, nome: str):
        self.nome: str = nome
        self.catalogo: List[Libro] = []

    def in_catalogo(self, *libri: Libro) -> None:
        """
        Aggiunge uno o più libri al catalogo della biblioteca.
        """
        self.catalogo.extend(libri)

    def stampa_cat(self) -> None:
        """
        Stampa tutti i libri presenti nel catalogo.
        """
        print(f"Catalogo della biblioteca '{self.nome}':")
        for libro in self.catalogo:
            print(libro)

    def write_csv(self, filename: str = 'catalogo.csv') -> None:
        """
        Scrive il catalogo della biblioteca su un file CSV.
        Sovrascrive il file se già esistente.
        """
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(['titolo', 'autore'])
            for libro in self.catalogo:
                writer.writerow([libro.titolo, libro.autore])

# --- Script Execution ---
if __name__ == '__main__':
    l1 = Libro('Esercizi', 'Dino Bianchi')
    l2 = Libro('Manuale', 'Luca Verdi')
    l3 = Libro('Faust', 'W. Goethe')
    l4 = Libro('Il capitale', 'K. Marx')
    l5 = Libro('Canne al vento', 'G. Deledda')

    b1 = Biblioteca('BiblioComunale')
    b2 = Biblioteca('Museale')

    b1.in_catalogo(l1, l2, l3)
    b2.in_catalogo(l4, l5)

    b2.stampa_cat()
    b1.stampa_cat()

    # Scrive due file separati per ciascuna biblioteca
    b1.write_csv('catalogo_biblio_comunale.csv')
    b2.write_csv('catalogo_museale.csv')