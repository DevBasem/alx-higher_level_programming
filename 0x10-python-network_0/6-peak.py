#!/usr/bin/python3
""" Find a peak in a list of unsorted integers """


def find_peak(list_of_integers):
    """ Find a peak in a list of unsorted integers """
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        # Check if mid is a peak
        if list_of_integers[mid] > list_of_integers[mid + 1] and list_of_integers[mid] > list_of_integers[mid - 1]:
            return list_of_integers[mid]

        # Move towards the higher end
        if list_of_integers[mid] < list_of_integers[mid + 1]:
            low = mid + 1
        else:
            high = mid - 1

    # Handle the case where the peak is at the last element
    return list_of_integers[low]
