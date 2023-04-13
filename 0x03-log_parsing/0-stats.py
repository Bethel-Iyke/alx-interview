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


status_dict = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 405: 0, 500: 0}
stdin = sys.stdin
counter = 0
total_file_size = 0

try:
    for line in stdin:
        output = line.split()
        if int(output[-2]) in status_dict.keys() and len(output) == 9:
            counter += 1
            status_dict[int(output[-2])] += 1
            total_file_size += int(output[-1])
        if counter % 10 == 0:
            print('File size: {}'.format(total_file_size))
            for key, value in status_dict.items():
                if value:
                    print("{}: {}".format(key, value))
except KeyboardInterrupt as error:
    print('File size: {}'.format(total_file_size))
    for key, value in status_dict.items():
        print("{}: {}".format(key, value))
