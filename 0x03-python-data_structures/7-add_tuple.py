#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a + (0, 0)
    b = tuple_b + (0, 0)
    sum_first = a[0] + b[0]
    sum_second = a[1] + b[1]
    result = (sum_first, sum_second)
    return result
