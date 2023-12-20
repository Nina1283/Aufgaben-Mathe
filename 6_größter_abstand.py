import math 

numbers_list = []
numbers_list2 = []
numbers_list3 = []

def get_numbers_list():
    _list = []
    try:
        count = int(input("Amount of numbers: "))

    except ValueError:
        print("The entry was not valid.")
        return
    

    for i in range(count):
        try:
            numbers = int(input("number: "))
            _list.append(numbers)
        
        except ValueError:
            print("The entry was not valid.")
    return _list

def max_difference(got_a_list):
    max_number = max(got_a_list)
    min_number = min(got_a_list)
    return max_number - min_number

numbers_list = get_numbers_list()
numbers_list2 = get_numbers_list()
numbers_list3 = get_numbers_list()

print(f"The max difference is {max_difference(numbers_list)}")
print(f"The max difference is {max_difference(numbers_list2)}")
print(f"The max difference is {max_difference(numbers_list3)}")