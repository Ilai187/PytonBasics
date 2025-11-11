import os

while True:
    z = input("Zahl: ")
    q = sum(int(x) for x in z if x.isdigit())

    print(f"- Quersumme: {q}")
    print(f"- Teilbar durch 3: {'Ja' if q%3==0 else 'Nein'}")
    print(f"- Teilbar durch 9: {'Ja' if q%9==0 else 'Nein'}")

    if input("- Weitere [j/n]: ") != "j":
        break
    os.system('cls')
