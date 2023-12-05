#!/usr/bin/python3
"""
101-stats module

Reads input from stdin line by line and computes metrics.

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
                                        <status code> <file size>
Every 10 lines and after a keyboard interruption (CTRL + C), it prints:
- Total file size: File size: <total size>
- Number of lines by status code:
  - Possible status codes: 200, 301, 400, 401, 403, 404, 405, 500
  - Format: <status code>: <number>, printed in ascending order
"""
import sys

if __name__ == "__main__":
    total_size = 0
    status_counts =
    {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

    def check_match(line):
        '''Checks for regexp match in line.'''
        try:
            line = line[:-1]
            words = line.split(" ")
            size = int(words[-1])
            code = int(words[-2])
            if code in status_counts:
                status_counts[code] += 1
            return size
        except ValueError:
            return 0

    def print_stats():
        '''Prints accumulated statistics.'''
        print("File size: {}".format(total_size))
        for code in sorted(status_counts.keys()):
            if status_counts[code]:
                print("{}: {}".format(code, status_counts[code]))

    line_count = 1
    try:
        for line in sys.stdin:
            total_size += check_match(line)
            if line_count % 10 == 0:
                print_stats()
            line_count += 1
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
