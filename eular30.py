if __name__ == "__main__":
def eular30():
    POWER = 5
    i = 0
    while True:
        if not functions.writable_by_powers(i, POWER):
            break
        i += 1

    print('Max number writable by fifth powers is {}'.format(i))

    fifth_sums = []
    for x in range(2, i + 1):
        if functions.sum_powers(x, POWER) == x:
            fifth_sums.append(x)

    print('These are the numbers that can be written as the sum of 5th powers of their digits.')
    print(fifth_sums)

    print('The sum of these numbers = {}'.format(sum(fifth_sums)))
