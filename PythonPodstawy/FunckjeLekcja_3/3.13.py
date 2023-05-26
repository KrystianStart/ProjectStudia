def main():
    x = 0
    while(x != 2):

        def tr():
            a = int(input('Dlugosc pierwszego boku trójkąta: '))
            h = int(input('Dlugosc wysokości trójkąta: '))
            return a * h / 2

        def pro():
            a = int(input('Dlugosc pierwszego boku prostokata: '))
            b = int(input('Dlugosc drugiego boku prostokata: '))
            return a * b

        def kol():
            r = int(input('Podaj długość promienia: '))
            return 3.14 * (r * r)

        def tra():
            a = int(input('Dlugosc pierwszej podstawy trapezu: '))
            b = int(input('Dlugosc drugiej podstawy trapezu: '))
            h = int(input('Wysokosc trapezu: '))
            return (a + b) * h / 2

        def kwa():
            a = int(input('Dlugosc boku kwadratu: '))
            return a * a

        def tr_ru():
            a = int(input('Dlugosc pierwszego boku trójkąta: '))
            h = int(input('Dlugosc wysokości trójkąta: '))
            return a * h / 2
        print(''''Wybierz figurę której pole chcesz wyświetlić: 
        
    [1] Trójkąt
    [2] Prostokąt
    [3] Koło
    [4] Trapez
    [5] Kwadrat
    [6] Trójkąt równoboczny''')
        y = int(input())
        if y == 1:
            print("Pole: ", tr())
        elif y == 2:
            print("Pole: ", pro())
        elif y == 3:
            print("Pole: ", kol())
        elif y == 4:
            print("Pole: ", tra())
        elif y == 5:
            print("Pole: ", kwa())
        elif y == 6:
            print("Pole: ", tr_ru())
        else:
            print("Podano inną liczbę")
        print('''Czy chesz odpalić znów program?:
    
    [1] Tak
    [2] Nie''')
        x = int(input())
main()