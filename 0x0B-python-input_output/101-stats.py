#!/usr/bin/python3
"""
Reads stdin line by line, computes metrics,
and prints statistics every 10 lines
and after a keyboard interruption (CTRL + C).

Metrics:
- Total file size: File size: <total size>
  (sum of file sizes from previous lines, see input format above)
- Number of lines by status code:
  - Possible status codes: 200, 301, 400, 401, 403, 404, 405, 500
  - Format: <status code>: <number>, printed in ascending order
"""
import sys

file_size = 0
status_tally = {"200": 0, "301": 0, "400": 0, "401": 0,
                "403": 0, "404": 0, "405": 0, "500": 0}
line_count = 0

try:
    for line in sys.stdin:
        tokens = line.split()
        if len(tokens) >= 2 and tokens[-2] in status_tally:
            status_tally[tokens[-2]] += 1
            try:
                file_size += int(tokens[-1])
            except Exception:
                continue
        line_count += 1
        if line_count % 10 == 0:
            print("File size: {:d}".format(file_size))
            for key, value in sorted(status_tally.items()):
                if value:
                    print("{:s}: {:d}".format(key, value))
    print("File size: {:d}".format(file_size))
    for key, value in sorted(status_tally.items()):
        if value:
            print("{:s}: {:d}".format(key, value))

except KeyboardInterrupt:
    print("File size: {:d}".format(file_size))
    for key, value in sorted(status_tally.items()):
        if value:
            print("{:s}: {:d}".format(key, value))
