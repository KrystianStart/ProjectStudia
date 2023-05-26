print("Podaj długości boku trójkąta:")
z = float(input())
x = float(input())
c = float(input())
if (z * z) + (x * x) == (x * x):
    print("Można utowrzyć trójkąt prostokątny")
elif (z * z) + (c * c) == (x * x):
    print("Można utowrzyć trójkąt prostokątny")
elif (x * x)  + (c * c) == (z * z):
    print("Można utowrzyć trójkąt prostokątny")
else:
    print("Nie da się utrworzyć trójkąta")