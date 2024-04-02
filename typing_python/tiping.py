import typing
import csv
#Modellazione classi

#la sintassi nome_variabile: tipo = valore defisce in origine il tipo  e come sotto funziona con la composizione di oggetti.
class libro:
    def __init__(self, titolo, autore):
        self.titolo: str = titolo# sintassi del modulo typing
        self.autore: str = autore

    def __repr__(self):
        return f"il libro: {self.titolo}, {self.autore}"
    
    def __str__(self) -> str:
        return f"{self.titolo}, {self.autore}"

        

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.catalogo: list[libro] = []# composizione di classi diverse

    def in_catalogo(self, *libro):#l'asterisco intende che si possono inserire più oggetti libro come parametri
        self.catalogo.append(libro)
    #la funzione __repr__ della classe libro passa la str a questa funzione stampa_cat
    def stampa_cat(self, *args):
        for l in self.catalogo:
            print(l)
    # funzione per scrivere file csv.
    def write_csv(self):
        fields = ['titolo', 'autore']
        with open('catalogo.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(fields)
            for row in self.catalogo:
                writer.writerows([row])


#Esecuzione script
l1 = libro('Esercizi', 'Dino Bianchi')
l2 = libro('Manuale', 'Luca Verdi')
l3 = libro('Faust', 'W. Goethe')
l4 = libro('Il capitale', 'K. Marx')

b1 = Biblioteca('BiblioComunale')

#b1.in_catalogo(l3, l2, l1)# qui si vede che la presenza dell'asterisco consente un inserimento multiplo di oggetti libro.
b1.in_catalogo(l1)
b1.in_catalogo(l2)
b1.in_catalogo(l3)

l5 = libro('Canne al vento', 'G. Deledda')
b2 = Biblioteca('Museale')
b2.in_catalogo(l4)
b2.in_catalogo(l5)

b2.stampa_cat()
b1.stampa_cat()
b1.write_csv()
b2.write_csv()