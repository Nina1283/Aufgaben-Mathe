def calculate_digit_sum(get_number):        #get_number = Übergabeparameter
    result = 0
   
    for every_digit in get_number:
        result +=  int(every_digit)
    return result                       #result = integer   

number = input("Write a number: ")

while len(number) > 1:
    print(f"The digit sum is: {calculate_digit_sum(number)}")       #number wird an calculate_digit_sum übergeben

    number = str(calculate_digit_sum(number))       #da result in der Funktion ein Integer ist u. die Funktion len nicht mit integern funktioniert, wird result zu einem string




