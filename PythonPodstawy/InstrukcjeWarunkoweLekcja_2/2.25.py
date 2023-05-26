waga = float(input("Wpisz swoją wagę w kg: "))
wzrost = float(input("Podaj swój wzrost w m:  "))
BMI = waga / float(wzrost * wzrost)
if BMI > 24.9:
    print("nadwaga")
elif BMI < 18.5:
    print("niedowaga")
else:
    print("waga jest prawidłowa")