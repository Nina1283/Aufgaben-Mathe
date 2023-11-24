import time
grenze = int(input("Gib eine Zahl ein, bis zu der zu Primzahlen ausgegeben bekommen willst: "))

liste = []
def primzahl_erkennen(grenze):                          
    
    for i in range(2, grenze+1):        
        is_no_primzahl = False      
        for j in liste:                    
            if i % j == 0:                          # am Anfang mit 2 % 0 wird j nicht ausgeführt, da die Liste leer ist, 
                is_no_primzahl = True     
                #break                              
        
        if is_no_primzahl == False:     
            liste.append(i)                         # is_no_primzahl ist nicht True und wird von daher zur Liste hinzugefügt
        
    #return liste                        

startTime = time.time()
print(f"Primzahlen: {primzahl_erkennen(grenze)}")
endTime = time.time()
processTime = endTime - startTime
print(processTime)   