
stunden = int(input("Gib Stunden ein: "))
minuten = int(input("Gib Minuten ein: "))
sekunden = int(input("Gib Sekunden ein: "))
gesamtstunden = stunden + (minuten / 60) + (sekunden / 3600)
print("Zeit in Stunden:", gesamtstunden)
