power = 5
bignine = 9 ** power


def writable_by_powers(n, p):
    digits = len(str(n))
    max_amt = digits * (9 ** p)
    if max_amt < n:
        return False
    else:
        return True


def sum_powers(n, p):
    return sum(int(x) ** p for x in str(n))

if __name__ == "__main__":
    POWER = 5
    i = 0
    while True:
        if not writable_by_powers(i, POWER):
            break
        i += 1

    print('Max number writable by fifth powers is {}'.format(i))

    fifth_sums = []
    for x in range(2, i + 1):
        if sum_powers(x, POWER) == x:
            fifth_sums.append(x)

    print('These are the numbers that can be written as the sum of 5th powers of their digits.')
    print(fifth_sums)

    print('The sum of these numbers = {}'.format(sum(fifth_sums)))
