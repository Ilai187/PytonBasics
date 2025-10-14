zahl1 = int(input("Zahl 1: "))
zahl2 = int(input("Zahl 2: "))
if zahl2 < zahl1 and zahl1 > 5:
    temp = zahl1
    zahl1 = zahl2
    zahl2 = temp
else:
    if zahl1 == zahl2:
        zahl1 = 5
    zahl2 = 8
print("Ausgabe 1 =", zahl1)
print("Ausgabe 2 =", zahl2)

#Bei 6 und 3 werden die beiden Zahlen vertauscht also Zahl eins wird zu Zahl 3 und Zahl 2 zu Zahl 6
#Bei dem 7 & 7 werden die beiden Zahlen am ende als 5(Zahl 1) und 8(Zahl 2) ausgegeben