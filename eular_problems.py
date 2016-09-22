import text
import factors
import fibseries


def separator():
    print('#'*80)


def eular1():
    print(text.eular1)
    result = factors.sum_multiples([3, 5], 1000)
    print('Sum = {}'.format(result))


def eular2():
    print(text.eular2)
    UPPERLIMIT = 4000000
    fibsum = sum([x for x in fibseries.fibonacci(UPPERLIMIT) if x % 2 == 0])
    print('Sum = {}'.format(fibsum))

if __name__ == "__main__":
    eular1()
    separator()
    eular2()
    separator()
