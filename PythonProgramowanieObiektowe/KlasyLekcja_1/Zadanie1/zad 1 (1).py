import math

class FunkcjaKwadratowa:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.delta = (self.b*self.b)-(4*self.a*self.c)

    def Rozwiaz(self):
        if self.delta < 0:
            print("Funkcja nie ma miejsc zerowych")

        elif self.a == 0 and self.b == 0 and self.c == 0:
            print("Podano wartości zerowe")

        elif self.b == 0 and self.c == 0:
            print("Liczba nieskończona")

        elif self.a == 0:
            x = -zmienna.c / zmienna.b
            print("Funckja jest liniowa, jej miejsce zerowe to:", x)

        else:
            x_1 = (-zmienna.b + math.sqrt(zmienna.delta)) / 2 * zmienna.a
            x_2 = (-zmienna.b - math.sqrt(zmienna.delta)) / 2 * zmienna.a

            if self.delta == 0:
                print("Funkcja ma jedno rozwiązanie:", int (x_1))
            else:
                print("Miejsca zerowe:", int(x_1), int(x_2))

zmienna = FunkcjaKwadratowa(0, 2, 1)

print(FunkcjaKwadratowa.Rozwiaz(zmienna))
