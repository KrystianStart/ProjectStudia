plik = open("liczby.txt", "w")
y = 0
for x in range(10):
    y = y + 1
    plik.write(str(y)+"\n")
plik.close()

kill = open("liczby.txt", "a")
slo = "ABCDEFGHIJKLMOPERSTUWXYZ"
for i in slo:
    kill.write(i+"\n")
kill.close()