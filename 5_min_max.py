import math

def get_numbers_list():
    global numbers_list
    numbers_list = []
    
    try:
     count = int(input("Count of numbers: "))

    except ValueError:
        print("Die Eingabe war nicht gültig.")
        return []

    for i in range(count):
        try:
            numbers = int(input("number: "))

        except ValueError:
            print("Die Eingabe war nicht gültig.")
            return []
        numbers_list.append(numbers)
    
    return numbers_list


get_numbers_list()


def calculate_min_and_max():
    min_numbers = min(numbers_list)
    max_numbers = max(numbers_list)
    print(f"Minimum: {min_numbers}") 
    print(f"Maximum: {max_numbers}") 


calculate_min_and_max()