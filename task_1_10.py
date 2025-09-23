distanz = float(input("Welche Distanz (KM) willst du auf deiner Reise zurücklegen? "))
tempo = float(input("Wie Schnell wirst du durchschnittlich fahren? "))
benzin = float(input("Wie hoch wird der Benzienverbrauch auf 100KM sein? "))
fahrzeits = distanz / tempo
fahrzeitm = fahrzeits * 60
gesamtverbrauch = (distanz / 100) * benzin

print(f"\nFahrzeit: {fahrzeitm:.1f} Minuten")
print(f"Gesamtverbrauch: {gesamtverbrauch:.2f} Liter")

