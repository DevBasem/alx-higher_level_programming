#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    results = []
    for number in my_list:
        is_multiple_of_2 = number % 2 == 0
        results.append(is_multiple_of_2)
    return results
