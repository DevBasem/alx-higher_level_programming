#!/usr/bin/python3
"""
101-stats module

This script reads input from stdin line by line and computes metrics.

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
                                        <status code> <file size>
Each 10 lines and after a keyboard interruption (CTRL + C),
it prints the following statistics since the beginning:
- Total file size: File size: <total size>
- Number of lines by status code:
    - Possible status codes: 200, 301, 400, 401, 403, 404, 405, and 500
    - If a status code doesn’t appear, it doesn’t print anything
    for that status code
    - Format: <status code>: <number>
    - Status codes are printed in ascending order
"""

import sys

if __name__ == "__main__":
    size = 0
    codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    def check_match(line):
        '''Checks for regexp match in line.'''
        try:
            line = line[:-1]
            words = line.split(" ")
            size += int(words[-1])
            code = int(words[-2])
            if code in codes:
                codes[code] += 1
        except ValueError:
            pass

    def print_stats():
        '''Prints accumulated statistics.'''
        print("File size: {}".format(size))
        for k in sorted(codes.keys()):
            if codes[k]:
                print("{}: {}".format(k, codes[k]))

    i = 1
    try:
        for line in sys.stdin:
            check_match(line)
            if i % 10 == 0:
                print_stats()
            i += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
