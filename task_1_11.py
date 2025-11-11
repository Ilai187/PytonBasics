#BMI = Gewicht (kg) ÷ [Größe (m)]²

grösse = float(input("Bitte gib deine Körpergrösse ein [Meter] "))
gewicht = float(input("Bitte gib dein Körpergewicht ein [KG] "))

bmi = gewicht/ (grösse ** 2)

print("Dein BMI ist:", bmi)