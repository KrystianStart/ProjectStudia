from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, skin, weight):
        self.skin = skin
        self.weight = weight

    @abstractmethod
    def kolory(self):
        pass

class Human(Animal):
    def __init__(self, hair, skin, eyes, weight, height):
        super().__init__(skin, weight)
        self.hair = hair
        self.eyes = eyes
        self.height = height

    def kolory(self):
        return self.hair, self.skin, self.eyes

    def dlugosci(self):
        print(self.weight, self.height)

    def wszystkie(self):
        print(self.hair, self.skin, self.eyes, self.weight, self.height)

    def duze_litery(self):
        self.hair = self.hair.upper()
        return self.hair


    def ocena_wagi(self):
        if int(self.weight) > 100:
            self.weight = "Gruby"
            return self.weight
        else:
            self.weight = "W normie"
            return self.weight

    @property
    def BMI(self):
        self.wskaznik_BMI = int(self.weight / (self.height*self.height))
        return print(self.wskaznik_BMI)

class Cat(Animal):
    def __init__(self, paws_lengh, skin, species, blood, weight):
        super().__init__(skin, weight)
        self.paws_lenght = paws_lengh
        self.species = species
        self.blood = blood

    def kolory(self):
        print(self.skin)

    def dlugosci(self):
        print(self.paws_lenght, self.weight)


    def wszystkie(self):
        print(self.paws_lenght, self.skin, self.species, self.blood, self.weight)

    def uzupelnienie_krwi(self):
        self.blood = "RH" + str(self.blood)
        return self.blood

    def czy_to_puma(self):
        if int(self.paws_lenght) > 10:
            self.paws_lenght = "To puma"
        else:
            self.paws_lenght = "Zwykly kocur"
            return self.paws_lenght

    def DNA(self):
        if "+" in str(self.blood) == True and self.weight > 30:
            self.weight = int(self.weight) + 10
            return self.weight
        elif "-" in str(self.blood) == True and self.weight <= 30:
            self.weight = int(self.weight) - 10
            return self.weight
        else:
            return self.weight

class UFO(Animal):
    def __init__(self, skin, weight, iq):
        super().__init__(skin, weight)
        self.iq = iq

    def kolory(self):
        print(self.skin)

    def tendecja_podbicia_swiata(self):
        if int(self.weight * self.iq) > 500 and self.skin != 'black':
            teskt = 'Podbije swiat'
            print(teskt)
            return teskt
        else:
            tekst = "Ludzie wygraja"
            print(tekst)
            return tekst


def main():
    hair = "blue"
    skin = "brown"
    eyes = "green"
    weight = 87
    height = 180
    zmienna_1 = Human(hair, skin, eyes, weight, height)
    zmienna_1.ocena_wagi()
    zmienna_1.wszystkie()

    paws_lenght = 6
    skin = "black"
    species = "faraon"
    blood = "+"
    weight = 50
    zmienna_2 = Cat(paws_lenght, skin, species, blood, weight)
    zmienna_2.uzupelnienie_krwi()
    zmienna_2.wszystkie()

    skin = "blue"
    weight = 70
    iq = 210
    zmienna_3 = UFO(skin, weight, iq)
    zmienna_3.tendecja_podbicia_swiata()


main()

"""
Dziedziczenie:
Aktywna możliwość przekazania wspólnych cech wielu klasą, minusem jest 

Polimorfia:
Możliwość wywołania metod w różnych klasach, minusem jest to że trzeba ją wszędzie zawrzec. Wyskakiwał mi błąd

Hermetyzacja:
Zabezpieczenie niepoprawnych wartości podanych przez użytkownika, plus możliwośc implementacji nowych pól. 
"""