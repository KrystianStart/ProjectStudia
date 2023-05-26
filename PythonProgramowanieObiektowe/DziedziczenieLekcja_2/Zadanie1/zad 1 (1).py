import math


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


zmienna = FunkcjaKwadratowa(0, -1, 1)

zmienna.rozwiaz()
