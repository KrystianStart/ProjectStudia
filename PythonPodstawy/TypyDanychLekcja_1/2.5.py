dane = [1, 1, 3, 2, 4, 6, 5, 3, 2, 1, 6, 50, 2, 3]

print(dane)
print(len(dane))
print(dane[0:3])
print(f"Dla 1: {dane.count(1)} Dla 2: {dane.count(2)} Dla 3: {dane.count(3)}")
print(6 in dane)
dane.insert(dane[3], -100)
print(dane)
del dane[-1]
print(dane)
dane.remove(50)
print(dane)
dane.pop(0)
print(dane)
dane2 = dane
dane2.reverse()
print(dane2)
dane3 = dane
dane3.sort()
print(dane3)