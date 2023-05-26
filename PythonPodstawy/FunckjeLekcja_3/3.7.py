print("""Wybiersz opcję zmiany skali:
1.Z Fahrenheita na Celsjusza
2.Z Celcjusza na Fahrenheita
""")
x = int(input())
if x == 1:
    def cel():
        '''
        Przy przeliczaniu skali Fahrenheita na Celsjusza
        '''
        c = int(input("Podaj wartość"))
        f = (c - 32) * (5 / 9)
        print(f)


    cel()
elif x == 2:
    def fah():
        """
        Przy przeliczaniu skali Celcjusza na Fahrenheita
        """
        f = int(input("Podaj wartość"))
        c = (f * (9 / 5)) + 32
        print(c)


    fah()
else:
    print("Podano zły znak")
