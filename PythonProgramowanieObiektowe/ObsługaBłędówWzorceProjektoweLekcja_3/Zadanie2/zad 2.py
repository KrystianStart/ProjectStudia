class Rabat:
    def oblicz_rabat(self, cena):
        pass


class RabatPracowniczy(Rabat):
    def oblicz_rabat(self, cena):
        return cena / (1 / cena)


class DarmowaDostawa(Rabat):
    def oblicz_rabat(self, cena):
        return cena - 10


class JedzeniePlus(Rabat):
    def oblicz_rabat(self, cena):
        return 0

class Zakup:
    def __init__(self, rabat):
        self.rabat = rabat

    def oblicz(self, cena):
        return cena - self.rabat.oblicz_rabat(cena)

cena1 = Zakup(RabatPracowniczy())
cena2 = Zakup(DarmowaDostawa())
cena3 = Zakup(JedzeniePlus())

cena = 200

print("Cena z rabatem pracowniczym: ", cena1.oblicz(cena))
print("Cena z darmowa dostawa: ", cena2.oblicz(cena))
print("Cena z nowym projektem JedzeniePlus ,,love social'': ", cena3.oblicz(cena))

"""
Fajnie pozwala na zmiane tak naprawde dzialania podczas trwania projektu, mozna tworzyc unikatowe 
algorytmy dla danych grup. Możliwość szybgiego przywolania. 

"""

class Polecenie:
    def wykonaj(self):
        pass

    def cofnij(self):
        pass

class DodajProduktPolecenie(Polecenie):
    def __init__(self, koszyk, produkt):
        self.koszyk = koszyk
        self.produkt = produkt

    def wykonaj(self):
        self.koszyk.dodaj_produkt(self.produkt)

    def cofnij(self):
        self.koszyk.usun_produkt(self.produkt)

class UsunProduktPolecenie(Polecenie):
    def __init__(self, koszyk, produkt):
        self.koszyk = koszyk
        self.produkt = produkt

    def wykonaj(self):
        self.koszyk.usun_produkt(self.produkt)

    def cofnij(self):
        self.koszyk.dodaj_produkt(self.produkt)

class ZlozZamowieniePolecenie(Polecenie):
    def __init__(self, koszyk):
        self.koszyk = koszyk

    def wykonaj(self):
        self.koszyk.zloz_zamowienie()

    def cofnij(self):
        self.koszyk.anuluj_zamowienie()

class Koszyk:
    def __init__(self):
        self.produkty = []

    def dodaj_produkt(self, produkt):
        self.produkty.append(produkt)
        print("Dodano produkt do koszyka:", produkt)

    def usun_produkt(self, produkt):
        if produkt in self.produkty:
            self.produkty.remove(produkt)
            print("Usunięto produkt z koszyka:", produkt)

    def zloz_zamowienie(self):
        print("Zamówienie złożone!")

    def anuluj_zamowienie(self):
        print("Anulowano zamówienie!")

"""
Polecenie analogicznie do strategi pozwala na stworzenie dużej ilości metod zależnych od Siebie, charakteryzuje się 
zdefiniowaną metodą miedzy którymi potem dokonujemy wyboru. Można tworzyć proste koszyki
"""


from abc import ABC, abstractmethod

class TaxCalculator(ABC):
    @abstractmethod
    def get_tax_rate(self):
        pass

    def calculate_tax(self, income):
        tax_rate = self.get_tax_rate()
        tax = income * tax_rate
        return tax

class PolandTaxCalculator(TaxCalculator):
    def get_tax_rate(self):
        return 0.20

class USATaxCalculator(TaxCalculator):
    def get_tax_rate(self):
        return 0.30

class GermanyTaxCalculator(TaxCalculator):
    def get_tax_rate(self):
        return 0.25

poland_calculator = PolandTaxCalculator()
usa_calculator = USATaxCalculator()
germany_calculator = GermanyTaxCalculator()

income = 100000

poland_tax = poland_calculator.calculate_tax(income)
usa_tax = usa_calculator.calculate_tax(income)
germany_tax = germany_calculator.calculate_tax(income)

print(f"Podatek w Polsce: {poland_tax}")
print(f"Podatek w USA: {usa_tax}")
print(f"Podatek w Niemczech: {germany_tax}")

"""
Dzieki metodzie szablonowej okreslamy szkielet algorytmu w klasie bazowej mogac korzystac z niego w klasach
pochodnych optymalizujac nasz kod i skracajac go. 
"""