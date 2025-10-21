
t = int(input("Tag: "))
m = int(input("Monat: "))
j = int(input("Jahr: "))

if m <= 2:
    m += 10
    j -= 1
else:
    m -= 2

c = j // 100
j = j % 100


h = int((((26 * m - 2) // 10) + t + j + j / 4 + c / 4 - 2 * c) % 7)

if h < 0:
    h += 7

tage = ["Sonntag", "Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag", "Samstag"]

print(f"Der {t}.{m}.{(c*100 + j)} ist ein {tage[h]}.")
