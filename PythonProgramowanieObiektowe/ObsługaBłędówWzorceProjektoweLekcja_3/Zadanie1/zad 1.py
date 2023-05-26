import math


def bledy():
    # Wyłapuje błąd typu danej, np kiedy  potrzebujemy obiektu do obliczeń
    try:
        x = int(input("Podaj liczbe calkowita \n"))
        print(x)

    except ValueError:
        print("...    Podano zla wartosc")

    # Zatrzymuje przed podaniem złego zakresu, bardzo podobne do KeyError można zauważyć dużą analogie
    try:
        tic = ['1', '2', '3', '4', '5']
        ind = tic[10]
        print(ind)
    except IndexError:
        print("Podano niewlasciwy index")


class Funkcja:
    def __init__(self, b, c):
        self.b = b
        self.c = c

    def rozwiaz(self):
        if self.b == 0 and self.c == 0:
            print("Nieskonczenie wiele rozwiazan")

        elif self.b == 0 and self.c != 0:
            print("Funkcja posida jedno miejsce zerowe", self.c)

        else:
            x = -self.c / self.b
            print("Funckja jest liniowa, jej miejsce zerowe to:", x)


class FunkcjaLiniowa(Funkcja):
    def rozwiaz(self):
        Funkcja.rozwiaz(self)


class FunkcjaKwadratowa(Funkcja):
    def __init__(self, b, c, a):
        super().__init__(b, c)
        self.a = a
        self.delta = (self.b * self.b) - (4 * self.a * self.c)

    def rozwiaz(self):
        if self.delta < 0:
            print("Funkcja nie ma miejsc zerowych")
        elif self.a == 0:
            super().rozwiaz()
        else:
            x_1 = (-self.b + math.sqrt(self.delta)) / (2 * self.a)
            x_2 = (-self.b - math.sqrt(self.delta)) / (2 * self.a)
            if self.delta == 0:
                print("Funkcja ma jedno rozwiązanie:", int(x_1))
            else:
                print("Miejsca zerowe:", int(x_1), int(x_2))
                try:
                    lista = [x_1, x_2]
                    wyb = int(input("Podaj indeks 0 lub 1"))
                    print(lista[wyb])

                except ValueError:
                    print("zle")

                except IndexError:
                    print('zle')


while True:
    try:
        y = int(input("Podaj liczbe \n"))
        if y < 0:
            raise Exception("Tylko dodatnie lub zero")
        else:
            break

    except ValueError:
        print("Podano zla wartosc")

zmienna = FunkcjaKwadratowa(y, y * y, y + 100)

assert zmienna.rozwiaz(), ['Cos nie zadzialalo']

