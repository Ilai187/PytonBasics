monat = int(input("Gib den aktuellen Monat ein [1-12]:"))
if monat <= 3:
    print ("Es ist Winter")
elif monat <= 6:
    print("Es ist frühling")
elif monat <= 9:
    print ("Es ist Sommer")
elif monat <= 12: 
    print ("Es ist Herbst")
else:
    print("Ungültige Zahl / Eingabe")
    