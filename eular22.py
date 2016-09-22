#!/usr/bin/env python3
# coding=utf-8
from __future__ import print_function


def import_names(filename):
    # Each name is contained in quotes ("NAME")
    # and also separated by commas("NAME1", "NAME2, "NAME3")

    names = []
    newname = ''
    with open(filename) as f:

        while True:
            char = f.read(1)
            if not char:
                break  # Empty string means EOF

            # Start a new name with each quote
            if char == "\"" and newname != '':
                names.append(newname)
                newname = ''
            elif char == "\"" or char == ',':
                # Ignore formatting characters
                continue
            else:
                newname += char

    # To sort we can merely use the builtin sorted()
    return sorted(names)


def alphabetical_value(name):
    return sum([ord(x.lower()) - 96 for x in list(name)])


if __name__ == "__main__":
    names = import_names('names.txt')

    print('names has {} entries.'.format(len(names)))

    namescore = 0

    for i, n in enumerate(names):
        namescore += alphabetical_value(n) * (i+1)

    print('The total of all name scores = {}'.format(namescore))
