class Human:
    def __init__(self, hair, skin, eyes, weight, height):
        self.hair = hair
        self.skin = skin
        self.eyes = eyes
        self.weight = weight
        self.height = height

    def kolory(self):
        print(self.hair, self.skin, self.eyes)

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

    def BMI(self):
        self.wskaznik_BMI = int(self.weight / (self.height*self.height))
        return self.wskaznik_BMI

class Cat:
    def __init__(self, paws_lenght, skin, species, blood, weight):
        self.paws_lenght = paws_lenght
        self.skin = skin
        self.species = species
        self.blood = blood
        self.weight = weight

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


def main():
    hair = "blue"
    skin = "brown"
    eyes = "green"
    weight = 87
    height = 180
    zmienna_1 = Human(hair, skin, eyes, weight, height)
    zmienna_1.ocena_wagi()
    print(zmienna_1.wszystkie())

    paws_lenght = 6
    skin = "black"
    species = "faraon"
    blood = "+"
    weight = 50
    zmienna_2 = Cat(paws_lenght, skin, species, blood, weight)
    zmienna_2.uzupelnienie_krwi()
    print(zmienna_2.wszystkie())

main()