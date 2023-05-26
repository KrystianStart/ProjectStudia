import csv
import os
import pandas as pd
from datetime import datetime


class Funkcje:

    # sprawdzanie  polskich znaków, metoda zwraca poprawną wartość
    @staticmethod
    def sprawdz_polskie_znaki():
        polskie_znaki = ['ą', 'ć', 'ę', 'ł', 'ń', 'ó', 'ś', 'ź', 'ż', 'Ą', 'Ć', 'Ę', 'Ł', 'Ń', 'Ó', 'Ś', 'Ź', 'Ż']
        while True:
            tekst = input()
            if any(znak in tekst for znak in polskie_znaki):
                print("[Kasia]: Wprowadzony tekst zawiera polskie znaki. Proszę wprowadzić tekst bez polskich znaków.")
            else:
                return tekst

    # zwraca poprawne wartości w inputach w granicach
    @staticmethod
    def wybor(y):
        while True:
            try:
                wybor = int(input())
                if 0 < wybor <= y:
                    return wybor
                else:
                    print("Podaj poprawna wartosc")
                    pass
            except ValueError:
                print("Podaj poprawna wartosc")
                pass

    @staticmethod
    def start():
        print("""[Kasia]: Witaj, wybierz opcje:
    [1] Dodaj ksiazke
    [2] Wypozyczyc ksiazke
    [3] Oddac ksiazka
    [4] Historia ksiazek
    [5] Wyjdz
    """)
        return Funkcje.wybor(5)

    #metoda sprawdza ilosc książek i dodaje do nich jeden u danej osoby
    @staticmethod
    def dekrementacja(numer):
        czy = pd.read_csv('czytacze.csv')
        if str(numer) in str(list(czy['Numer czytacza'])):
            dek = int(czy.iat[numer - 1, 3]) + 1
            return dek
        else:
            return 1

    # metoda zwraca index
    @staticmethod
    def indeks():
        column_names = ["ID", "Tytul", "Autor", "Rok wydania", "Status"]
        df = pd.read_csv('biblioteka.csv', names=column_names)
        numery = df.ID.to_list()
        naj_id = numery.pop()
        ind = int(naj_id) + 1
        return ind

    # metoda sprawdza czy liczba
    @staticmethod
    def liczba():
        while True:
            try:
                rok = int(input())
                return rok
            except ValueError:
                print("[Kasia]: Nie podano liczby")
                continue

    # formatowanie do daty z wykorzystaniem)
    @staticmethod
    def data():
        while True:
            data = input("[Kasia]: Podaj date w formacie dd/mm/rrrr: ")
            try:
                data = datetime.strptime(data, "%d/%m/%Y")
                return data
            except ValueError:
                print("[Kasia]: Nieprawidlowy format daty. Sprobuj ponownie.")

    # zwraca idex znajdujdujący wartość dla inputa
    @staticmethod
    def idx_tytul():
        while True:
            with open('biblioteka.csv', 'r'):

                bib = pd.read_csv('biblioteka.csv')

                wys = input("[Kasia]: \n Podaj tytul lub numer indeksu \n")

                idx = 0

                for _, row in bib.iterrows():
                    if str(row[0]) == wys and row[4] == 'Nie w bibliotece':
                        return idx
                    idx += 1

                ilc = 0
                idx = 0

                for _, row in bib.iterrows():
                    if str(row[1]) == wys and row[4] == 'Nie w bibliotece':
                        ilc += 1
                        continue
                    idx += 1

                if ilc > 1:
                    ind = input(print("[Kasia]: Jest wiecej niz jedna ksiazka, prosze o podanie indeksu \n"))
                    if ind in list(bib['ID']):
                        return ind
                    else:
                        print("[Kasia]: Zly indeks")
                        continue

                elif ilc == 1:
                    return idx

                else:
                    print("[Kasia]: Nie ma takiej ksiazki")


    @staticmethod
    def powrot_menu():
        print("[Kasia]: Czy chcesz wrocic do menu \n [1]Tak     [2]Nie \n")
        dec = Funkcje.wybor(2)
        match dec:
            case 1:
                main()
            case 2:
                pass

    @staticmethod
    def spr_zaw(dana):
        if os.path.isfile('czytacze.csv'):
            with open('czytacze.csv', 'r') as csvfile:
                while True:
                    column_names = ['Numer czytacza', 'Imie', 'Nazwisko', 'Ilosc ksiazek']
                    czy = pd.read_csv('czytacze.csv', usecols=column_names)
                    if str(dana) in str(list(czy['Numer czytacza'])):
                        print("[Kasia]: Numer czytacza sie powtarza, powtorz probe")
                        csvfile.close()
                        dana = input()

                    elif str(dana) in str(list(czy['Imie'])):
                        print("[Kasia]: Imie sie powtarza, powtorz probe")
                        csvfile.close()
                        dana = input()

                    else:
                        csvfile.close()
                        return dana
        else:
            return dana


    # maly konstruktor wywyolujace inne metody
    @staticmethod
    def dane_wyp():
        print("[Kasia]: \n Podaj numer czytacza \n")
        numer_czytacza = Funkcje.spr_zaw(Funkcje.sprawdz_polskie_znaki())
        print("[Kasia]: \n Podaj imie \n")
        imie = Funkcje.spr_zaw(Funkcje.sprawdz_polskie_znaki())
        print("[Kasia]: \n Podaj nazwisko \n")
        nazwisko = Funkcje.spr_zaw(Funkcje.sprawdz_polskie_znaki())
        data = Funkcje.data()
        Wypozyczenie.wez(Wypozyczenie(numer_czytacza, imie, nazwisko, data))


#cała klasa wypozycznie dziedzieczy inna wartosci, reszta przezksztalca
class Wypozyczenie:
    def __init__(self, numer_czytacza, imie, nazwisko, data):
        self.numer_czytacza = numer_czytacza
        self.imie = imie
        self.nazwisko = nazwisko
        self.data = data

    def wez(self):
        with open('biblioteka.csv', 'r+'):
            bib = pd.read_csv('biblioteka.csv')
            while True:
                wys = input("[Kasia]: \n Podaj tytul lub numer indeksu \n")

                znal = False

                idx = -1
                for item in str(list(bib['ID'])):
                    if item == wys and bib.iat[idx, 4] == 'W bibliotece':
                        bib.at[idx, 'Status'] = 'Nie w bibliotece'
                        znal = True
                        break
                    idx += 1

                if not znal:
                    idx = -1
                    for item in list(bib['Tytul']):
                        if item == wys and bib.iat[idx, 4] == 'W bibliotece':
                            bib.at[idx, 'Status'] = 'Nie w bibliotece'
                            znal = True
                            break
                        idx += 1

                if znal:
                    if int(bib.iat[idx, 3]) >= self.data.year:
                        print("[Kasia]: Data wczesniejsza niz wydanie ksiazki")
                        Wypozyczenie.historia(Wypozyczenie(self.numer_czytacza, self.imie, self.nazwisko, self.data),
                                              idx, False)
                    else:
                        print("[Kasia]: Wypozyczono")
                        bib.to_csv('biblioteka.csv', index=False)
                        Wypozyczenie.czytacze(Wypozyczenie(self.numer_czytacza, self.imie, self.nazwisko, self.data),
                                              idx)

                else:
                    print("[Kasia]: Nie ma takiej ksiazki lub zostala wypozyczona")
                    Wypozyczenie.historia(Wypozyczenie(self.numer_czytacza, self.imie, self.nazwisko, self.data), idx,
                                          False)

    def czytacze(self, idx):

        if not os.path.isfile('czytacze.csv'):

            struct = {'Numer czytacza': self.numer_czytacza,
                      'Imie': self.imie,
                      'Nazwisko': self.nazwisko,
                      'Ilosc ksiazek': 1}

            with open('czytacze.csv', 'w') as csvfile:
                fieldnames = ['Numer czytacza', 'Imie', 'Nazwisko', 'Ilosc ksiazek']
                csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
                csvwriter.writeheader()
                csvwriter.writerow(struct)
                csvfile.close()
                Wypozyczenie.historia(Wypozyczenie(self.numer_czytacza, self.imie, self.nazwisko, self.data), idx,
                                      True)
        else:
            with open('czytacze.csv', 'r+') as csvfile:
                writer = csv.writer(csvfile)
                dek = Funkcje.dekrementacja(self.numer_czytacza)
                writer.writerow([self.numer_czytacza, self.imie, self.nazwisko, dek])
                Wypozyczenie.historia(Wypozyczenie(self.numer_czytacza, self.imie, self.nazwisko, self.data), idx, True)
                csvfile.close()

    def historia(self, idx, czy_udana):

        self.data = f"{self.data.day}/{self.data.month}/{self.data.year}"

        if not os.path.isfile('historia.csv'):

            if not czy_udana:
                struct = {'ID': idx,
                          'Numer czytacza': self.numer_czytacza,
                          'Czy udana': 'Nie',
                          'Data wypozyczenia': self.data,
                          'Data oddania': '-'}
            else:
                struct = {'ID': idx,
                          'Numer czytacza': self.numer_czytacza,
                          'Czy udana': 'Tak',
                          'Data wypozyczenia': self.data,
                          'Data oddania': '-'}

            with open('historia.csv', 'w') as csvfile:
                fieldnames = ['ID', 'Numer czytacza', 'Czy udana', 'Data wypozyczenia', 'Data oddania']
                csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
                csvwriter.writeheader()
                csvwriter.writerow(struct)
                csvfile.close()
            Funkcje.powrot_menu()

        else:
            with open('historia.csv', 'a') as csvfile:
                if not czy_udana:
                    writer = csv.writer(csvfile)
                    writer.writerow([idx, self.numer_czytacza, "Nie", self.data, "-"])
                    csvfile.close()
                else:
                    writer = csv.writer(csvfile)
                    writer.writerow([idx, self.numer_czytacza, "Tak", self.data, "-"])
                    csvfile.close()
                Funkcje.powrot_menu()


class Oddac:
    @staticmethod
    def daj():
        ind = int(Funkcje.idx_tytul())
        while True:
            data = Funkcje.data()
            with open('historia.csv', 'r+') as csvfile:
                his = pd.read_csv('historia.csv')
                if datetime.strptime(his.iat[ind, 3], "%d/%m/%Y").year > data.year:
                    print("[Kasia]: Data oddania wczesniejsza niz wypozyczenia")
                    csvfile.close()
                    continue

                try:
                    if datetime.strptime(his.iat[ind, 4], "%d/%m/%Y") > data:
                        print("[Kasia]: Data wypozyczenia wczesniejsza niz oddania")
                        csvfile.close()
                        continue

                except ValueError:
                    his.at[ind, 'Data oddania'] = f"{data.day}/{data.month}/{data.year}"
                    his.to_csv('historia.csv', index=False)
                    csvfile.close()
                    Funkcje.powrot_menu()
                    break

                else:
                    his.at[ind, 'Data oddania'] = f"{data.day}/{data.month}/{data.year}"
                    his.to_csv('historia.csv', index=False)
                    csvfile.close()
                    Funkcje.powrot_menu()
                    break

        with open('biblioteka.csv', 'r+') as csvfile:
            bib = pd.read_csv('biblioteka.csv')
            bib.at[ind, 'Status'] = 'W bibliotece'
            bib.to_csv('biblioteka.csv', index=False)
            csvfile.close()


class Biblioteka:

    @staticmethod
    def dodaj():
        print("[Kasia]: \n Podaj tytul \n")
        tytul = Funkcje.sprawdz_polskie_znaki()
        print("[Kasia]: \n Podaj autora \n")
        autor = Funkcje.sprawdz_polskie_znaki()
        print("Podaj rok wydania: \n")
        rok_wydania = Funkcje.liczba()
        status = 'W bibliotece'

        if not os.path.isfile('biblioteka.csv'):

            struct = {'ID': 1,
                      'Tytul': tytul,
                      'Autor': autor,
                      'Rok wydania': rok_wydania,
                      'Status': status}

            with open('biblioteka.csv', 'w') as csvfile:
                fieldnames = ['ID', 'Tytul', 'Autor', 'Rok wydania', 'Status']
                csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
                csvwriter.writeheader()
                csvwriter.writerow(struct)
                csvfile.close()
        else:
            ind = Funkcje.indeks()

            with open('biblioteka.csv', 'a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([ind, tytul, autor, rok_wydania, status])
                csvfile.close()
        Funkcje.powrot_menu()

    @staticmethod
    def historia():
        ind = Funkcje.idx_tytul()
        his = pd.read_csv('historia.csv')
        for row in his.iterrows():
            if row[0] == ind:
                print(row)
        Funkcje.powrot_menu()


def main():
    while True:
        wybor = Funkcje.start()
        match wybor:
            case 1:
                Biblioteka.dodaj()
            case 2:
                if os.path.isfile('biblioteka.csv'):
                    Funkcje.dane_wyp()
                else:
                    print("[Kasia]: Nie posiadamy jeszcze zadnej ksiazki")
                    continue
            case 3:
                if os.path.isfile('biblioteka.csv'):
                    Oddac.daj()

                else:
                    print("[Kasia]: Nie posiadamy jeszcze zadnej ksiazki")
                    continue
            case 4:
                if os.path.isfile('biblioteka.csv'):
                    Biblioteka.historia()
                else:
                    print("[Kasia]: Nie posiadamy jeszcze zadnej ksiazki")
                    continue
            case 5:
                exit(0)


if __name__ == '__main__':
    main()
