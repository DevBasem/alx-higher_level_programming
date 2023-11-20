#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    index = 0
    new_list = []
    division_result = 0
    for index in range(0, list_length):
        try:
            division_result = (my_list_1[index] / my_list_2[index])
        except TypeError:
            division_result = 0
            print("wrong type")
        except ZeroDivisionError:
            division_result = 0
            print("division by 0")
        except IndexError:
            division_result = 0
            print("out of range")
        finally:
            new_list.append(division_result)
    return new_list
