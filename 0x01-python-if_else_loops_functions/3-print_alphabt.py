#!/usr/bin/python3
for char_code in range(ord('a'), ord('z') + 1):
    if char_code == ord('q') or char_code == ord('e'):
        continue
    else:
        print("{}".format(chr(char_code)), end='')
