"""
Eular Problem13: *Large Sum*
Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
"""


def read_numbers(filename):
    """
    Read each number as a line from the file and return the numbers as a list.
    """
    numbers = []
    with open(filename) as f:
        for l in f.readlines():
            numbers.append(int(l))

    return numbers

if __name__ == "__main__":
    n = read_numbers('bignumbers.txt')
    bigsum = 0
    for x in n:
        bigsum += x
        print(x)

    print('sum = {}'.format(bigsum))
    sum_list = list(str(bigsum))
    first_ten_digits = sum_list[-10:]
    print(first_ten_digits)
