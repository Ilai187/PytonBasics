Geschlecht = input("Gib dein Geschlecht ein [m/w]: ").lower()
Gewicht = int(input("Gib dein Gewicht ein [KG]: "))

if Geschlecht == "m":
    if Gewicht <= 55:
        print("Gewichtsklasse: Fliegengewicht")
elif Gewicht <= 66:
    print("Gewichtsklasse: Leichtgewicht")    
elif Gewicht <= 84:
    print("Gewichtsklasse: Mittelgewicht")
else:
    print("Gewichtsklasse: Schwergewicht")
    
if Geschlecht == "w":
    if Gewicht <= 48:
        print("Gewichtsklasse: Fliegengewicht")
elif Gewicht <= 55:
        print("Gewichtsklasse: Leichtgewicht")
elif Gewicht <= 63:
        print("Gewichtsklasse: Mittelgewicht")
elif Gewicht <= 85:
        print("Gewichtsklasse: Schwergewicht")

else:
    print("Ungültige Eingabe beim Geschlecht.")