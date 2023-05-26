punkty = int(input("Podaj liczbę punktów do 50: "))
procenty = float(punkty * 2)
if procenty > 100:
    print("Źle podane punkty")
elif procenty > 99:
    print("cel")
elif procenty > 84:
    print("bdb")
elif procenty > 69:
    print("db")
elif procenty > 49:
    print("dst")
elif procenty > 39:
    print("dop")
else:
    print("ndst")


