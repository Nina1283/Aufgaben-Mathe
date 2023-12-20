def calculate_digit_sum(get_number):        #get_number = Übergabeparameter
    result = 0
   
    for every_digit in get_number:
        result +=  int(every_digit)
    return result

number = input("Write a number: ")

print(f"The digit sum is: {calculate_digit_sum(number)}")       #number wird an calculate_digit_sum übergeben

