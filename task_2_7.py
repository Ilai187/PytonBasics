jahr = int(input("Gib ein Jahr ein: "))

m = (8 * (jahr // 100) + 13) // 25 - 2
s = jahr // 100 - jahr // 400 - 2
m = (15 + s - m) % 30
n = (6 + s) % 7

a = jahr % 19
b = jahr % 4
c = jahr % 7
d = (19 * a + m) % 30
if d == 29:
    d = 28
elif d == 28 and a >= 11:
    d = 27
e = (2 * b + 4 * c + 6 * d + n) % 7

ostertag = 22 + d + e
if ostertag > 31:
    ostertag = ostertag % 31
    ostermonat = "April"
else:
    ostermonat = "März"
    
print(f"Ostern fällt im Jahr {jahr} auf den {ostertag}. {ostermonat}.")
