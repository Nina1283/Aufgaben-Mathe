import math

def get_numbers_list():
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


def calculate_average(numbers_list):
    sum_of_numbers = sum(numbers_list)
    count_of_numbers = len(numbers_list)

    average = sum_of_numbers/count_of_numbers

    return average

numbers_list = get_numbers_list()

if numbers_list:
   average = calculate_average(numbers_list)
   print(f"Mittelwert: {average}")

