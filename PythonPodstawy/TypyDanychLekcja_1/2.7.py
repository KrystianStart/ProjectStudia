dane = (1, 1, 3, 2, 4, 6, 5, 3, 2, 1, 6, 50, 2, 3)
print(len(dane))
print(dane.count(1), dane.count(2), dane.count(3))
print(50 in dane)
lista = list(dane)
lista.insert(lista[4], 300)
lista.insert(lista[5], 200)
lista.insert(lista[6], 100)
dane = lista
print(dane)

