def des():
    krotka = (3132, 8423, 4528, 5121, 9348)
    print(krotka[0], krotka[-1])
    lista = list(krotka)
    lista[0] = 2
    del lista[-1]
    krotka = lista
    print(krotka)

des()
