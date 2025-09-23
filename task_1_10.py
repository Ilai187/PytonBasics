distanz = float(input("Welche Distanz (KM) willst du auf deiner Reise zurücklegen? "))
tempo = float(input("Wie Schnell wirst du durchschnittlich fahren? "))
benzin = float(input("Wie hoch wird der Benzienverbrauch auf 100KM sein? "))
fahrzeits = distanz / tempo
fahrzeitm = fahrzeits * 60
gesamtverbrauch = (distanz / 100) * benzin

print("Fahrzeit:", round(fahrzeitm, 1), "Minuten")
print("Verbrauch:", round(gesamtverbrauch, 2), "Liter")

