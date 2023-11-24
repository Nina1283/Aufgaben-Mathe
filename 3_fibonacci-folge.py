liste = []
limit = int(input("Gebe eine Grenze ein: "))


def fibonacci_folge(liste): 
    x, y = 1, 1
    liste.append(x)
    liste.append(y)

    for i in range(limit-2):
        z = x + y
        liste.append(z)
        x = y 
        y = z
    return liste

print(f"Fibonacci-Folge: {fibonacci_folge(liste)}")
