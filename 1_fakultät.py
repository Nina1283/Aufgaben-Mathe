from math import factorial

zahl = int(input("Gebe eine Zahl ein, von der du die Fakultät berechnen möchtest: "))


def fakultät_berechnen():
    if zahl < 0:
        print("Die Fakultät einer negativen Zahl existiert nicht.")
        return zahl
    
    else:
        fakultät = factorial(zahl)
        print(f"Die Fakultät von {zahl} lautet", fakultät)
        return fakultät

fakultät_berechnen()


    