def statistic(lista):
    print("Suma: ", sum(lista))
    print("Różnica: ", sum(lista) / len(lista))
    lista.sort()
    print("Najmniejsza wartość: ", lista.pop(0))
    print("Największa wartość: ", lista.pop(-1))
