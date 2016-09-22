from __future__ import print_function
import factors


if __name__ == "__main__":
    print('Eular project 25')
    LIMIT = 28123
    abundants = [i for i in range(1, LIMIT + 1) if factors.is_abundant(i)]
    sums = set([a + abundants[b]
                for i, a in enumerate(abundants)
                for b in range(i, len(abundants))])
    unsummable = [i for i in range(LIMIT + 1) if i not in sums]

    print('Sum of all positive ints which can\'t be summed by 2 abundants={}'.format(
        sum(unsummable)))
