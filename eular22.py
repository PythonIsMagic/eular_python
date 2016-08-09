#!/usr/bin/env python3
# coding=utf-8

"""
++ Eular22
*Names scores*

Using names.txt, a 46K text file containing over five-thousand first names,
begin by sorting it into alphabetical order. Then working out the alphabetical
value for each name, multiply this value by its alphabetical position in the
list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is
worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would
obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

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
