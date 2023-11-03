#!/usr/bin/python3
def magic_calculation(a, b):
    if a < b:
        from magic_calculation_102 import add
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    else:
        from magic_calculation_102 import sub
        return sub(a, b)
