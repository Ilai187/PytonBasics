riegel = 3.20
geld = 20
rest = (geld % riegel)
anzahl = (geld // riegel)
print(round(rest))
print (anzahl)


zahl1 = float(input("Gib eine Zahl ein: "))
zahl2 = float(input("Gib eine zweite Zahl ein: "))

if zahl1 > zahl2:
    print("Zahl1 ist grösser")
elif zahl1 < zahl2:
    print("Zahl2 ist grösser")
else:
    print("Die Zahlen sind gleichgross")


zahl = float(input("Gib eine Zahl ein: "))

if zahl >= 10 and zahl <= 20:
    print("Die Zahl liegt zwischen 10 und 20.")
else:
    print("Die Zahl liegt nicht zwischen 10 und 20.")

if zahl < 0 or zahl > 100:
    print("Die Zahl ist kleiner als 0 oder grösser als 100.")
else:
    print("Die Zahl liegt zwischen 0 und 100.")
