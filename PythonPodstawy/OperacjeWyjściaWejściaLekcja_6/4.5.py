y = 0

while y != 1:
    print("""Wybierz opcję:
    [D] Dodaj
    [U] Usuń
    [W] Wypisz
    [Q] Wyjdź """)
    x = input()
    def dod():
        plik = open("dane.txt", "a")
        x = input("Podaj imię: ")
        y = input("Podaj nazwisko: ")
        z = input("Podaj stanowisko: ")
        a = input("Podaj wynagrodzenie: ")
        plik.write(x+" "+y+" "+z+" "+a+"\n")
        plik.close()

    def usu():
        with open("dane.txt") as plik:
            naz = input("Podaj nazwisko: ")
            plik = open("dane.txt", "r")
            linie = plik.readlines()
        plik = open("dane.txt", "w")
        for wiersz in linie:
            naz2 = wiersz.split(" ")[1]
            if naz != naz2:
                plik.write(wiersz)
            else:
                print("Imię usunięte")
        plik.close()

    def wyp():
        with open("dane.txt") as fp:
            text = fp.read()
            print("Zawartość pliku:"+"\n", text)

    if x == 'D':
        dod()
    elif x == 'U':
        usu()
    elif x == 'W':
        wyp()
    elif x == 'Q':
        y = y + 1