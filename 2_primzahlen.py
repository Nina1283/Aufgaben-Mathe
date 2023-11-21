liste = []
def primzahl_erkennen(grenze):
    
    for i in range(2, grenze+1):
        is_no_primzahl = False
        for j in liste:
            if i % j == 0:
                is_no_primzahl = True

        if is_no_primzahl == False:
            liste.append(i)
        
    return liste

print(primzahl_erkennen(89))
