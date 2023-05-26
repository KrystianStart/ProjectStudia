class Punkt:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(f"Utworzono punkt ({self.x},{self.y})")

    def wyswietl(self):
        print(f"Wspolrzedne punktu to: ({self.x},{self.y})")


    def pobierzX(self):
        return self.x

    def pobierzY(self):
        return self.y

    def ustawXY(self, Punkt):
        self.x = Punkt.x
        self.y = Punkt.y

    def pobieszWsp(self):
        return self.x, self.y

class Test:
    def main():

        x = 2
        y = 5
        Punkt(x, y).wyswietl()

        x = 4
        y = 6
        Punkt(x, y).wyswietl()

        x = 6
        y = 7
        Punkt(x, y)



    if __name__ == "__main__":
        main()

"""
9. Podczas tworzenia obiektu klasy Punkt konstruktor wypisał na konsoli komunikat 
10. Podczas tworzenia obiektu bez argumentu konstruktor odrzuca możliwość pobrania danych wymagając 2 argumentów
"""