#!/usr/bin/python3
""" 0. Log parsing """
import sys

counter = {"total_size": 0, "nb_line": 1}
status_codes = {'200': 0, '301': 0, ' 400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}


def print_stats():
    print('File size: {}'.format(counter["total_size"]))
    for key in sorted(status_codes.keys()):
        if status_codes[key]:
            print('{}: {}'.format(key, status_codes[key]))

try:
    for line in sys.stdin:
        try:
            line_in_list = line.split(" ")
            file_size = int(line_in_list[-1])
            status_code = line_in_list[-2]
        except:
            pass

        if status_code in status_codes:
            status_codes[status_code] += 1
            counter["total_size"] += file_size
            counter["nb_line"] += 1
        if counter["nb_line"] % 10 == 0:
            print_stats()
except KeyboardInterrupt:
    pass
finally:
    print_stats()
