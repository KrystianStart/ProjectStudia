a = float(input("Podaj a:"))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))
trojman = b*b - 4*a*c
if trojman == 0:
    print("równanie ma dokładnie jedno rozwiązanie")
elif trojman > 0:
    print("równanie ma dwa rozwiązania")
else:
    print("równanie nie ma rozwiązań")
