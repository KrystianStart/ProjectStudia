print("Podaj długości boku trójkąta:")
z = float(input())
x = float(input())
c = float(input())
if z + x == c:
    print("Można utworzyć trójkąt")
elif z + c == x:
    print("Można utworzyć trójkąt")
elif x + c == z:
    print("Można utworzyć trójkąt")
else:
    print("Nie da się utworzyć trójkąta")