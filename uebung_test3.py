note1 = float(input("Gib eine Note ein: "))
note2 = float(input("Gib eine zweite Note ein: "))
note3 = float(input("Gib eine dritte Note ein: "))

durchschnitt = (note1 + note2 + note3) / 3

if durchschnitt >= 4:
    print("Die Note", durchschnitt ,"ist genügend")
else:
    print("Die Note", durchschnitt ,"ist Ungenügend")




a , b , c = 1 , 3 , "Hallo"
print(a)
print(b)
print(c)