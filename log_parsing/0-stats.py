#!/usr/bin/python3
""" 0. Log parsing """
import sys

count = {"total_size": 0, "nb_line": 1}
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}


def print_stats():
    print('File size: {}'.format(count["total_size"]))
    for key in sorted(status_codes.keys()):
        if status_codes[key]:
            print('{}: {}'.format(key, status_codes[key]))

try:
    for line in sys.stdin:
        try:
            line_in_list = line.split(" ")
            ip_adress_list = line_in_list[0].split(".")

            # check the format of the line.
            if len(line_in_list) == 9 and len(ip_adress_list) == 4:
                file_size = int(line_in_list[-1])
                status_code = line_in_list[-2]

                # check if status code is valid.
                if status_code in status_codes:
                    status_codes[status_code] += 1
                    count["total_size"] += file_size

                    # every 10 lines, print stats
                    if count["nb_line"] != 0 and count["nb_line"] % 10 == 0:
                        print_stats()
                    count["nb_line"] += 1
        except:
            pass
except KeyboardInterrupt:
    raise
finally:
    print_stats()
