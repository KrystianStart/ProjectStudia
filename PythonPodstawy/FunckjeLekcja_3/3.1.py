print("Podaj dwie liczby")
liczba1 = input()
liczba2 = input()
znak = str(input("Podaj znak (+, -, *, /): "))
if type(liczba1) != float:
        if type(liczba2) != float:
                print("Nie podana liczby")
elif znak == "+":
        print(liczba1 + liczba2)
elif znak == "-":
        print(liczba1 - liczba2)
elif znak == "*":
        print(liczba1 * liczba2)
elif znak == "/":
        print(liczba1 / liczba2)
else:
        print("Podano zły znak")