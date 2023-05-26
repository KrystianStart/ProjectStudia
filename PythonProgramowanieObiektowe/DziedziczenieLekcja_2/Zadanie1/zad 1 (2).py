class Ulamek:
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik

    def skroc(self, a, b):

        while b > 0:
            r = a % b
            a = b
            b = r

        return self.licznik//a, self.mianownik//a

    @staticmethod
    def dodaj(u1, u2):
        if u1.mianownik == u2.mianownik:
            return u1.licznik + u2.licznik, u1.mianownik + u2.mianownik
        else:
            licznik1 = u1.licznik * u2.mianownik
            licznik2 = u2.licznik * u1.mianownik
            return licznik1 + licznik2, u1.mianownik * u2.mianownik

    @staticmethod
    def odejmij(u1, u2):
        if u1.mianownik == u2.mianownik:
            return u1.licznik - u2.licznik, u1.mianownik - u2.mianownik
        else:
            licznik1 = u1.licznik * u2.mianownik
            licznik2 = u2.licznik * u1.mianownik
            return licznik1 - licznik2, u1.mianownik * u2.mianownik

    @staticmethod
    def mnoz(u1, u2):
        return u1.licznik * u2.licznik, u1.mianownik * u2.mianownik

    @staticmethod
    def dziel(u1, u2):
        return u1.licznik * u2.mianownik, u1.mianownik * u2.licznik

class UlamekZ(Ulamek):
    pass

class UlamekD(Ulamek):
    def __init__(self, licznik):
        mianownik = 1
        while (licznik != int(licznik)):
            licznik *= 10
            mianownik *= 10
            super().__init__(licznik, mianownik)


def main():
    a = 9
    b = 5
    u1 = Ulamek(licznik=a, mianownik=b)
    print("Ułamek po skróceniu: {}".format(u1.skroc(a, b)))

    a = 4
    b = 6
    u2 = Ulamek(licznik=a, mianownik=b)

    print("Suma ułamków: {}".format(Ulamek.dodaj(u1, u2)))
    print("Różnica ułamków: {}".format(Ulamek.odejmij(u1, u2)))
    print("Iloczyn ułamków: {}".format(Ulamek.mnoz(u1, u2)))
    print("Iloraz ułamków: {}".format(Ulamek.dziel(u1, u2)))

if __name__ == "__main__":
    main()