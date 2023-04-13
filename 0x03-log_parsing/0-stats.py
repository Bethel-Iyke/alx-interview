#!/usr/bin/python3
"""Script that reads from stdin line by line and computes metrics with the following:
Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
After every 10 lines and/or a keyboard interruption, print these statistics from the beginning:
Total file size which is the sum of all previous files with the following possible status code:
200, 301, 400, 401, 403, 404, 405 and 500.
if a status code doesn’t appear or is not an integer, don’t print anything for this status code
and it should be printed in ascending order.
"""

import re
import sys


stdin = sys.stdin
counter = 0
total_size = 0
status_code_counts = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        404: 0,
        405: 0,
        500: 0}
try:
    for line in stdin:
        counter += 1
        status_code = int(line.split()[-2])
        if status_code in status_code_counts:
            status_code_counts[status_code] += 1
            file_size = int(line.split()[-1])
            total_size += file_size
        if counter % 10 == 0:
            print("File size: {}".format(total_size))
            for code, count in status_code_counts.items():
                if count != 0:
                    print("{}: {}".format(code, count))
except KeyboardInterrupt as error:
    print("File size: {}".format(total_size))
    for code, count in status_code_counts.items():
        if count != 0:
            print("{}: {}".format(code, count))

