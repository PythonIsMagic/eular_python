"""Eular Problem 22 -
    Using names.txt, work out the alphabetical value for each name, multiply
    this value by its alphabetical position in the list to obtain a name
    score. What is the total of all the name scores in the file?
"""

import timer


DESC = 'Names scores'
SOLUTION = 871198282

def alphabetical_value(name):
    """ Returns the sum of the alphabetical values of the string passed. Each
        letter is equal to it's position in the alphabet.
        Example: COLIN is worth 3 + 15 + 12 + 9 + 14 = 53
    """
    return sum([ord(x.lower()) - 96 for x in list(name)])


def import_names(filename):
    """ Reads the names files from Project Eular(for problem 22) and loads each
        name into a list.
    """
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


@timer.timeit
def solve():

    names = import_names('data/names.txt')
    print('names has {} entries.'.format(len(names)))
    result = 0

    for i, n in enumerate(names):
        result += alphabetical_value(n) * (i+1)

    return result
